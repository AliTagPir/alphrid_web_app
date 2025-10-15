import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        token: localStorage.getItem('access_token') || null,
        user: JSON.parse(localStorage.getItem('user')) || null,
    }),
    getters: {
        isAuthenticated: (state) => !!state.token,
        isAdmin: (state) => state.user?.role === 'admin',
        isGuest: (state) => state.user?.role === 'guest'
    },
    actions: {
        setToken(token) {
            this.token = token
            localStorage.setItem('access_token', token)
        },
        setUser(user) {
            this.user = user
            localStorage.setItem('user', JSON.stringify(user))
        },
        logout() {
            this.token = null
            this.user = null
            localStorage.removeItem('access_token')
            localStorage.removeItem('user')
        },
         async fetchUserInfo() {
            if (!this.token) return

            try {
                const res = await fetch('http://localhost:8000/auth/me', {
                    headers: {
                        Authorization: `Bearer ${this.token}`,
                    }
                })

                if (!res.ok) throw new Error("Invalid token or user fetch failed")
                
                const user = await res.json()
                this.setUser(user)
            } catch (err) {
                console.error("Failed to fetch user info:", err)
                this.logout()
            }
        }
    }
})