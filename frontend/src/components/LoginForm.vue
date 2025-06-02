<script setup>
import { ref } from "vue";

const emit = defineEmits(["submit"]);
const props = defineProps({
  errorMessage: {
    type: String,
    default: "",
  },
});
const username = ref("");
const password = ref("");

const handleSubmit = () => {
  if (!username.value || !password.value) {
    emit("error", "Username and password are required");
    return;
  }
  emit("submit", { username: username.value, password: password.value });
};
</script>

<template>
  <div class="login-form">
    <div class="login-box">
      <form class="form" @submit.prevent="handleSubmit">
        <h2 class="login-title">Login to ALPHRID</h2>
        <div class="input-box">
          <span class="icon">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="size-6"
            >
              <path
                fill-rule="evenodd"
                d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z"
                clip-rule="evenodd"
              />
            </svg>
          </span>
          <input v-model="username" type="text" required />
          <label>Username</label>
        </div>

        <div class="input-box">
          <span class="icon">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              class="size-6"
            >
              <path
                fill-rule="evenodd"
                d="M12 1.5a5.25 5.25 0 0 0-5.25 5.25v3a3 3 0 0 0-3 3v6.75a3 3 0 0 0 3 3h10.5a3 3 0 0 0 3-3v-6.75a3 3 0 0 0-3-3v-3c0-2.9-2.35-5.25-5.25-5.25Zm3.75 8.25v-3a3.75 3.75 0 1 0-7.5 0v3h7.5Z"
                clip-rule="evenodd"
              />
            </svg>
          </span>
          <input v-model="password" type="password" required />
          <label>Password</label>
        </div>

        <button type="submit" class="login-button">Login</button>
        <transition name="fade">
          <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
        </transition>
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
  width: 500px;
  height: 450px;
  background: #4c4944;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 2px solid #e8e0cd;
}
.form {
  width: 75%;
  height: 75%;
}
.login-title {
  font-size: 1.8rem;
  color: #e8e0cd;
  text-align: center;
  padding-bottom: 20px;
}
.input-box {
  position: relative;
  width: 100%;
  margin: 30px 0;
  border-bottom: 2px solid #e8e0cd;
  padding: 0 50px 0 5px;
}
.input-box label {
  position: absolute;
  top: 50%;
  left: 5px;
  transform: translateY(-50%);
  font-size: 1rem;
  color: #e8e0cd;
  pointer-events: none;
  transition: 0.5s;
}

.input-box input:focus ~ label,
.input-box input:valid ~ label {
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
  margin-top: 10px;
  color: #e8e0cd;
}
.login-button {
  width: 100%;
  height: 15%;
  background: #e8e0cd;
  border: none;
  outline: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  color: #000000;
}
.error {
  color: red;
  font-size: 0.9rem;
  margin-top: 1rem;
  text-align: center;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Very Large Screens: 1440px and above */
@media (min-width: 2000px) {
  .login-box {
    width: 700px;
    height: 550px;
  }
  .form {
    height: 75%;
    font-size: 1.2rem;
  }
  .input-box .icon {
    right: 4px;
    width: 36px;
    margin-top: 2px;
  }
  .login-title {
    font-size: 2.5rem;
    color: #e8e0cd;
    text-align: center;
    padding-bottom: 20px;
  }
  .input-box {
    margin: 30px 0;
    border-bottom: 3px solid #e8e0cd;
    padding: 20px 50px 0 5px;
  }
  .input-box label {
    position: absolute;
    top: 50%;
    left: 5px;
    font-size: 1.5rem;
  }
  .login-button {
    font-size: 1.2rem;
  }
  .error{
    font-size: 1rem;
  }
}

@media (min-width: 768px) and (max-width: 1999px) {
  .login-box {
    width: 500px;
    height: 450px;
  }
}

/* 📱 Phones: below 768px */
@media (max-width: 767px) {
  .login-box {
    width: 100%;
    height: 60vh;
  }
}
</style>
