<script setup>
import {ref} from 'vue';

defineProps({
  buttonText: String,
  headerText: String,
});

const email = ref();
const password = ref();
</script>

<template>
  <div class='base-form'>
    <v-sheet>
      <v-form
          @submit.prevent="$emit('submit-form', { email, password })"
      >
        <div class='base-form__header'> {{ headerText }}</div>
        <v-text-field v-model="email" label="Email" type="email"></v-text-field>
        <v-text-field v-model="password" label="Password" type="password"></v-text-field>
        <v-btn block class="mt-2" type="submit">{{ buttonText }}</v-btn>
      </v-form>
    </v-sheet>
  </div>
</template>

<style scoped>
.base-form {
  position: absolute;
  display: flex;
  justify-content: center;
  top: 52%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 30%;
  height: 35%;
  text-align: center;
  z-index: 2;
}

.base-form__header {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 2rem;
}

:deep(.v-sheet) {
  width: 100%;
  height: 100%;
  background: #fff;
  border-radius: 10px;
  padding: 20px;
  font-size: 1.2rem;
}

:deep(.v-form) {
  width: 100%;
  height: 100%;
}
</style>
