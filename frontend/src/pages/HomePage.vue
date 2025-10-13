<script setup>
import Navbar from '@/components/Navbar.vue'
import { useAuthStore } from '@/stores/auth'
import { ref, onMounted } from 'vue'
import Plotly from 'plotly.js-dist-min'


const chartData = ref(null)
const authStore = useAuthStore()
const loading = ref(true)
const error = ref(null)



onMounted(async () => {
  try {
    const token = authStore.token
    if (!token) {
      error.value = 'No token found. Please log in.'
      loading.value = false
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
    chartData.value = data.chart_data

    //Dynamically renders the chart into div
    Plotly.newPlot('monthly-chart', chartData.value.data, chartData.value.layout)

  } catch (err) {
    error.value = `Error: ${err.message}`
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="home-page">
    <Navbar />
    <div class="content">
      <!-- Home page content here -->
      <h1>ALPHRID Monthly Chart JSON</h1>

      <div v-if="loading">Loading chart...</div>
      <div v-if="error" class="error">{{ error }}</div>

      <div v-show="!loading && !error" id="monthly-chart" style="width: 100%; height: 600px;"></div>
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