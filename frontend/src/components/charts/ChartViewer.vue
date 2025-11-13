<script setup>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth';

const props = defineProps({
  timeframe: {
    type: String,
    required: true
  }
});

const title = props.timeframe.toUpperCase();

const chartData = ref(null);
const currentKey = ref('');
const isLoading = ref(true);
const error = ref(null);

const authStore = useAuthStore();
console.log("Token from Pinia:", authStore.accessToken);
const token = authStore.accessToken;

const fetchChartKeys = async () => {
  const res = await fetch(`http://localhost:8000/charts/${props.timeframe}/keys`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  if (!res.ok) throw new Error(`Failed to fetch keys (${res.status})`);

  const data = await res.json();
  if (!data.keys || !data.keys.length) throw new Error("No chart keys found");

  return data.keys;
};

const fetchChartByKey = async (key) => {
  const res = await fetch(`http://localhost:8000/charts/key/${key}`, {
    headers: {
      Authorization: `Bearer ${token}`
    }
  });

  if (!res.ok) throw new Error(`Failed to fetch chart for key ${key} (${res.status})`);

  const data = await res.json();
  return data.chart_data;
};

onMounted(async () => {
  if (!token) {
    error.value = "No token found. Please log in.";
    isLoading.value = false;
    return;
  }

  try {
    const keys = await fetchChartKeys();
    currentKey.value = keys[keys.length - 1]; // Use the latest (last) key
    chartData.value = await fetchChartByKey(currentKey.value);
  } catch (err) {
    error.value = err.message;
  } finally {
    isLoading.value = false;
  }
});
</script>

<template>
  <div class="chart-viewer">
    <h2>{{ title }} Chart</h2>

    <div v-if="isLoading">Loading chart...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <p>Viewing: <strong>{{ currentKey }}</strong></p>
      <pre>{{ chartData }}</pre>
      <!-- You can replace this with a real chart later -->
    </div>
  </div>
</template>

<style scoped>
.chart-viewer {
  text-align: center;
  color: white;
}

.error {
  color: #f87171;
}
</style>