<script setup>
import {useStore} from 'vuex';
import BaseForm from '../components/BaseForm.vue';
import router from '../routes/index.js';

const store = useStore();

function handleLogin(data) {
  store
      .dispatch('logIn', {email: data.email, password: data.password})
      .then(() => router.push('/dashboard'))
      .catch((error) => {
        window.alert(error);
      });
}
</script>

<template>
  <div>
    <div class="img"></div>
    <BaseForm
        button-text='Login'
        header-text="Login Form"
        @submit-form='(data) => handleLogin(data)'
    />
  </div>
</template>

<style scoped>
.img {
  width: 100%;
  height: 100vh;
  background-size: auto;
  background-repeat: no-repeat;
  background: url('../assets/dogCatEating.png');
  position: relative;
}

.img::before {
  content: '';
  position: absolute;
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.4);
}
</style>
