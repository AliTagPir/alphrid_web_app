<script setup>
import ChartViewer from './ChartViewer.vue'
</script>

<template>
  <div class="monthly-chart-wrapper">
    <ChartViewer timeframe="monthly" />
  </div>
</template>

<style scoped>
.monthly-chart-wrapper {
  margin-top: 2rem;
}
</style>