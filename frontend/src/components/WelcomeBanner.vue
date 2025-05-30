
<template>
  <div class="welcome-banner">
    <div class="content">
      <h1>Welcome to ALPHRID</h1>
      <button @click="$emit('login-clicked')">Log In</button>
    </div>
  </div>
</template>

<style scoped>
.welcome-banner {
  height: 100vh;
  width: 100%;
  background: linear-gradient(135deg, #e8e0cd, #b4ad9f);
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  color: #000000;
  text-align: center;
}

.content h1 {
  font-size: 3rem;
  margin-bottom: 2rem;
}

button {
  padding: 0.75rem 2rem;
  background-color: #4c4944;
  color: #e8e0cd;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #000000;
}
</style>