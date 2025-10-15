<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import WelcomeBanner from '@/components/WelcomeBanner.vue'
import LoginForm from '@/components/LoginForm.vue'
import { useAuthStore } from '@/stores/auth'

const showLoginForm = ref(false)
const router = useRouter();
const errorMessage = ref('')
const authStore = useAuthStore()

const handleLogin = async ({ username, password }) => {
  try {
    const res = await fetch('http://localhost:8000/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json'},
      body: JSON.stringify({username, password})
    });

    const data = await res.json();
    
    if (res.ok) {
      authStore.setToken(data.access_token)
      await authStore.fetchUserInfo()
      router.push("/home");
    } else {
      errorMessage.value = data.detail || 'login failed';
      return
    } 
  } catch (err) {
    errorMessage.value = 'Invalid username or password'
  }
};
</script>

<template>
  <div class="login-page">
    <!-- Welcome Banner Div -->
    <transition name="slide-up">
      <div v-if="!showLoginForm" class="banner-wrapper">
        <WelcomeBanner @login-clicked="showLoginForm = true" />
      </div>
    </transition>

    <!-- Login Form Div -->
    <transition name="slide-in">
      <div v-if="showLoginForm" class="form-wrapper">
        <LoginForm :error-message="errorMessage" @submit="handleLogin" />
      </div>
    </transition>
  </div>
</template>

<style scoped>
.login-page {
  min-height: 100vh;
  width: 100vw;
  position: relative;
  background: #000;
}

.banner-wrapper, .form-wrapper {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

/* Slide-up animation (Banner leaving) */
.slide-up-leave-active {
  transition: all 0.8s ease;
}
.slide-up-leave-to {
  transform: translateY(-100%);
  opacity: 0;
}

/* Slide-in animation (Form appearing) */
.slide-in-enter-active {
  transition: all 0.8s ease;
}
.slide-in-enter-from {
  transform: translateY(100%);
  opacity: 0;
}
.slide-in-enter-to {
  transform: translateY(0);
  opacity: 1;
}
</style>
