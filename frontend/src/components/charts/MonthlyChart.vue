<script setup>
import ChartViewer from './ChartViewer.vue'

const customLayout = {
  title: {
    text: 'Monthly Productivity',
    font: { size: 24, color: '#ffffff' }
  },
  plot_bgcolor: '#1e1e2f',
  paper_bgcolor: '#1e1e2f',
  font: { color: '#ffffff' },
  margin: { t: 50, l: 30, r: 30, b: 30 }
}

const customConfig = {
  responsive: true,
  displayModeBar: false
}
</script>

<template>
  <ChartViewer
    timeframe="monthly"
    :layout="customLayout"
    :config="customConfig"
  />
</template>