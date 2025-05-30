<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { login } from '@/services/authService'

const username = ref('')
const password = ref('')
const errorMessage = ref('')
const router = useRouter()

const handleLogin = async () => {
    try {
    await login(username.value, password.value)
    router.push('/home')
  } catch (err) {
    errorMessage.value = 'Invalid username or password'
  }
}
</script>

<template>
  <div class="login-page">
    <h1 class="text-2xl mb-4">Login to ALPHRID</h1>
    <form @submit.prevent="handleLogin" class="space-y-4">
      <input
        v-model="username"
        type="text"
        placeholder="Username"
        class="w-full p-2 border rounded"
      />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        class="w-full p-2 border rounded"
      />
      <button
        type="submit"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Login
      </button>
      <p v-if="errorMessage" class="text-red-500">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<style scoped>
.login-page {
  max-width: 400px;
  margin: 100px auto;
  padding: 1rem;
}
</style>