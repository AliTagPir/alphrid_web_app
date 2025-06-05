<script setup>
</script>
<template>
  <nav class="navbar">
    <div class="logo">ALPHRID</div>
    <ul class="nav-links">
      <li><a href="#">Dashboard</a></li>
      <li><a href="#">Tracker</a></li>
      <li><a href="#">Logout</a></li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  width: 100%;
  background-color: #e8e0cd; /* Dark warm gray */
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.5);
}

.logo {
  font-size: 1.5rem;
  color: #000000; /* Light beige */
  font-weight: bold;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 2rem;
}

.nav-links li a {
  text-decoration: none;
  color: #807b71;
  font-size: 1rem;
  transition: color 0.3s;
}

.nav-links li a:hover {
  color: #4c4944; /* Soft hover */
}

.nav-links li a.active {
  color: #000000; /* Active link */
}
</style>
