<script setup>
import { onMounted } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
authStore.restoreSession()

</script>

<template>
  <router-view />
</template>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}



</style>
