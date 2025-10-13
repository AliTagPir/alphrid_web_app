<script setup>
import Navbar from '@/components/Navbar.vue'
import { useAuthStore } from '@/stores/auth'
import { ref, onMounted } from 'vue'


const chartJson = ref(null)
const authStore = useAuthStore()


onMounted(async () => {
  try {
    const token = authStore.token
    if (!token) {
      chartJson.value = 'Error: No token found. Please log in.'
      return
    }
    const res = await fetch("http://localhost:8000/charts/monthly", {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })

    if (!res.ok) {
      throw new Error("Failed to fetch chart")
    }

    const data = await res.json()
    chartJson.value = JSON.stringify(data.chart_data, null, 2)
  } catch (err) {
    chartJson.value = `Error: ${err.message}`
  }
})
</script>

<template>
  <div class="home-page">
    <Navbar />
    <div class="content">
      <!-- Home page content here -->
      <h1>Welcome to ALPHRID Dashboard</h1>
      <h1>ALPHRID Monthly Chart JSON</h1>

      <pre v-if="chartJson">{{ chartJson }}</pre>
      <p v-else>Loading chart...</p>
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