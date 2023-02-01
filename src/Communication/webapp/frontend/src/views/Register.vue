<script setup>
import { useStore } from 'vuex';
import BaseForm from '../components/BaseForm.vue';
import router from '../routes/index';

const store = useStore();

function handleRegister(data) {
  store
    .dispatch('register', { email: data.email, password: data.password })
    .then(() => router.push('/dashboard'))
    .catch((error) => {
      window.alert(error);
    });
}
</script>

<template>
  <div>
    <div class="img"></div>
    <div class="center">
      <BaseForm
          button-text='Register'
          header-text="Register Form"
          @submit-form='(data) => handleRegister(data)'
      />
    </div>
  </div>

</template>

<style scoped>
.img {
  background: url('../assets/dogs.jpg') no-repeat;
  width: 100%;
  height: 100vh;
  background-size: cover;
  background-position: center;
  position: relative;
}

.img::before {
  content: '';
  position: absolute;
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.4);
}

.center {
  position: absolute;
  display: flex;
  justify-content: center;
  top: 52%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  padding: 0 20px;
  text-align: center;
}
</style>
