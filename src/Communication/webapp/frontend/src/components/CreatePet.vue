<script setup>
import { ref } from 'vue';
import { useStore } from 'vuex';
import BaseButton from './BaseButton.vue';

const emit = defineEmits(['return-home']);

const name = ref();
const weight = ref();
const store = useStore();

function submitPet() {
  store.dispatch('addPet', { name, weight });
  emit('return-home');
}
</script>

<template>
  <div class='create-pet'>
    <div class='create-pet__wrapper'>
      <div class="icons">
        <font-awesome-icon :icon="['fa-solid', 'fa-dog']" class='dog-icon'/>
        <font-awesome-icon :icon="['fa-solid', 'fa-cat']" class='cat-icon'/>
      </div>
      <form class='form card' @submit.prevent='submitPet()'>
        <div class='field'>
          <label for='name'>Pet's name</label>
          <input
              id='email'
              v-model='name'
              class='input'
              placeholder='Name'
              required
              type='text'
          />
        </div>
        <div class='field'>
          <label for='weight'>Pet's weight</label>
          <input
              v-model='weight'
              class='input'
              placeholder='Weight'
              required
              type='number'
          />
        </div>
        <div class='field button_wrapper'>
          <BaseButton text='Add pet'/>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.create-pet {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.create-pet__wrapper {
  padding: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.icons {
  display: flex;
}

.dog-icon {
  margin-bottom: 90px;
  font-size: 100px;
}

.cat-icon {
  padding-left: 15px;
  margin-bottom: 90px;
  font-size: 100px;
}

input {
  font-size: 30px;
  max-width: 300px;
  margin-left: 30px;
  border-radius: 5px;
  padding-left: 20px;
}

.field {
  font-size: 40px;
  margin-bottom: 70px;
}

.button_wrapper {
  display: flex;
  justify-content: center;
}

button {
  font-size: 40px;
  padding: 10px;
  border-radius: 10px;
}
</style>
