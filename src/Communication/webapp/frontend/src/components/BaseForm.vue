<script setup>
import { ref } from 'vue';
import BaseButton from './BaseButton.vue';

defineProps({
  buttonText: String,
  headerText: String,
});

const email = ref();
const password = ref();
</script>

<template>
  <form class='form card' @submit.prevent="$emit('submit-form', { email, password })">
    <div class='card_header'>
      <h1 class='form_heading'>{{ headerText }}</h1>
    </div>
    <div class='field'>
      <label for='email'>Email</label>
      <input id='email' v-model='email' class='input' placeholder='Email' required type='email'>
    </div>
    <div class='field'>
      <label for='password'>Password</label>
      <input v-model='password' class='input' placeholder='Password' required type='password'>
    </div>
    <div class='field'>
      <BaseButton :text='buttonText' />
    </div>
  </form>
</template>

<style scoped>
.card {
  width: 400px;
  height: 350px;
  background: white;
  border: 1px solid whitesmoke;
  border-radius: 20px;
  box-shadow: 10px 10px 64px 0 rgba(180, 180, 207, 0.75);
  -webkit-box-shadow: 10px 10px 64px 0 rgba(186, 186, 202, 0.75);
  -moz-box-shadow: 10px 10px 64px 0 rgba(208, 208, 231, 0.75);

}

.form {
  padding: 25px;
}

.card_header {
  display: flex;
  align-items: center;
  justify-content: center;
}

.form_heading {
  padding-bottom: 20px;
}

.field {
  padding-bottom: 10px;
}

.input {
  border-radius: 5px;
  background-color: white;
  padding: 5px;
  width: 100%;
  height: 30px;
  color: black;
  border: 1px solid black
}

.input:focus-visible {
  outline: 1px solid black;
}

.input::placeholder {
  color: black;
}

label {
  color: black;
  display: block;
  padding-bottom: 4px;
  font-size: larger;
}

button {
  background-color: black;
  margin-top: 20px;
  width: 25%;
  height: fit-content;
  border-radius: 11px;
  font-size: larger;
  padding: 7px 12px;
  font-weight: 500;
  color: white;
}

button:hover {
  opacity: 0.6;
}
</style>
