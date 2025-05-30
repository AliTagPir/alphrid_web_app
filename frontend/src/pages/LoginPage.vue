<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import WelcomeBanner from '@/components/WelcomeBanner.vue'
import LoginForm from '@/components/LoginForm.vue'
import { login } from '@/services/authService'

const showLoginForm = ref(false)
const router = useRouter();

const handleLogin = async ({ username, password }) => {
  try {
    await login(username, password);
    router.push("/home");
  } catch (err) {
    console.error("Login failed", err);
    // Optional: Show a toast notification later
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
        <LoginForm @submit="handleLogin" />
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
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column
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
