import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        token: localStorage.getItem('access_token') || null,
        user: null
    }),
    getters: {
        isAuthenticated: (state) => !!state.token
    },
    actions: {
        setToken(token) {
            this.token = token
            localStorage.setItem('access_token', token)
        },
        setUser(User) {
            this.user = user
        },
        logout() {
            this.token = null
            this.user = null
            localStorage.removeItem('access_token')
        }
    }
})