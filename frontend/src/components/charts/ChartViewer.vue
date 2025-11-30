<script setup>
import { ref, onMounted, watchEffect } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { fetchChartKeysRequest, fetchChartByKeyRequest} from '@/services/chartApi';
import Plotly from 'plotly.js-dist-min'

const props = defineProps({
  timeframe: {
    type: String,
    required: true
  },
  layout: {
    type: Object,
    default: () => ({})
  },
  config: {
    type: Object,
    default: () => ({})
  }
})

const chartContainer = ref(null)
const title = props.timeframe.toUpperCase();
const chartData = ref(null);
const currentKey = ref('');
const isLoading = ref(true);
const error = ref(null);

const authStore = useAuthStore();
console.log("Token from Pinia:", authStore.token);
const token = authStore.token;


onMounted(async () => {
  if (!token) {
    error.value = "No token found. Please log in.";
    isLoading.value = false;
    return;
  }

  try {
    const keys = await fetchChartKeysRequest(props.timeframe, token);
    currentKey.value = keys[keys.length - 1]; // Use the latest (last) key
    const data = await fetchChartByKeyRequest(currentKey.value, token);
    chartData.value = data
    console.log(chartData.value)
    

  } catch (err) {
    error.value = err.message;
  } finally {
    isLoading.value = false;
  }
});

watchEffect(() => {
  const data = chartData.value;
  const container = chartContainer.value;

  if (data && container) {
    Plotly.newPlot(
      container,
      data.data,
      { ...data.layout, ...props.layout }, // merge server + custom
      props.config
    );
  }
});
</script>

<template>
  <div class="chart-viewer">
    <h2>{{ props.timeframe.toUpperCase() }} Chart</h2>

    <div v-if="isLoading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else>
      <p>Viewing: <strong>{{ currentKey }}</strong></p>
      <div ref="chartContainer" class="chart-container"></div>
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
.chart-container {
  width: 100%;
  height: 500px;
}
</style>