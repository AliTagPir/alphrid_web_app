<script setup>
import { ref } from "vue";
import userIcon from "@/assets/icons/userIcon.png";
import lockIcon from "@/assets/icons/lockIcon.png";

const emit = defineEmits(["submit"]); // ✅ emit submit event to parent
const username = ref("");
const password = ref("");
const errorMessage = ref("");

const handleSubmit = () => {
  if (!username.value || !password.value) {
    errorMessage.value = "Username and password are required";
    return;
  }
  errorMessage.value = "";
  emit("submit", { username: username.value, password: password.value });
};
</script>

<template>
  <div class="login-form">
    <div class="login-box">
      <form @submit.prevent="handleSubmit">
        <h2 class="login-title">Login to ALPHRID</h2>
        <div class="input-box">
          <span class="icon">
            <img :src="userIcon" alt="" class="icon" />
          </span>
          <input v-model="username" type="text" />
          <label>Username</label>
        </div>

        <div class="input-box">
          <span class="icon">
            <img :src="lockIcon" alt="" class="icon"/>
          </span>
          <input v-model="password" type="password" />
          <label>Password</label>
        </div>

        <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Login
        </button>
        <p v-if="errorMessage">{{ errorMessage }}</p>
      </form>
    </div>
  </div>
</template>

<style scoped>
.login-form {
  height: 100vh;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-box {
  position: relative;
  width: 400px;
  height: 500px;
  background-color: red;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-title {
  font-size: 1.8rem;
  color: #fff;
  text-align: center;
}
.input-box {
  position: relative;
  width: 310px;
  margin: 30px 0;
  border-bottom: 2px solid #fff;
}
.input-box label {
  position: absolute;
  top: 50%;
  left: 5px;
  transform: translateY(-50%);
  font-size: 1rem;
  color: #fff;
  pointer-events: none;
  transition: .5s;
}

.input-box input:focus~label,
.input-box input:valid~label {
    top: -5px;
}

.input-box input {
  width: 100%;
  height: 50px;
  background: transparent;
  border: none;
  outline: none;
  font-size: 1em;
  color: #fff;
}
.input-box .icon {
    position: absolute;
    right: 4px;
    width: 28px;
    margin-bottom: 2px;
    
}
</style>
