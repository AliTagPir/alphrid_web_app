<script setup>
import Navbar from '@/components/Navbar.vue'
</script>

<template>
  <div class="home-page">
    <Navbar />
    <div class="content">
      <!-- Home page content here -->
      <h1>Welcome to ALPHRID Dashboard</h1>
    </div>
  </div>
</template>

<style scoped>
.home-page {
  background-color: #000000; /* Black background */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.content {
  flex: 1;
  padding: 2rem;
  color: #e8e0cd; /* Light beige text */
}
</style>