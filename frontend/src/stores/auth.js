import { defineStore } from 'pinia'
import { loginRequest, fetchUserInfoRequest } from '@/services/authApi'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        token: null,
        user: null,
    }),
    getters: {
        isAuthenticated: (state) => !!state.token,
        isAdmin: (state) => state.user?.role === 'admin',
        isGuest: (state) => state.user?.role === 'guest'
    },
    actions: {
        async login({ username, password }) {
            try {
                const data = await loginRequest(username, password)
                this.setToken(data.access_token)
                await this.fetchUserInfo()
                return { success: true }
            } catch (err) {
                this.logout(); // ensure clean state
                return { success: false, message: err.message };
            }
        },
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
                const user = await fetchUserInfoRequest(this.token)
                this.setUser(user)
            } catch (err) {
                console.error("Failed to fetch user info:", err)
                this.logout()
            }
        },
        restoreSession() {
            const token = localStorage.getItem('access_token')
            const user = localStorage.getItem('user')

            if (token) {
                    this.setToken(token)
                if (user) {
                    this.setUser(JSON.parse(user))
                } else {
                    this.fetchUserInfo()
                }
            }
        }
        
    }
})