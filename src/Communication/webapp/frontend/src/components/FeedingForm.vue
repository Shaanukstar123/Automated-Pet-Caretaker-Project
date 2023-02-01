<script setup>
import { useStore } from 'vuex';
import { computed, defineEmits, ref } from 'vue';
import BaseButton from './BaseButton.vue';

const store = useStore();
const pets = computed(() => store.getters.petNames);
const date = ref();
const petName = ref(pets.value[0]);
const food = ref(0);
const emit = defineEmits(['goto-feedhistory']);
const feedingSchedule = ref('once');

function submitFood() {
  store.dispatch('addFeeding', {
    petName, food, date, feedingSchedule,
  });
  emit('goto-feedhistory');
}
</script>

<template>
  <div class='feeding-form'>
    <div class='feeding-from-wrapper'>
      <div class='icons'>
        <font-awesome-icon :icon="['fa-solid', 'fa-dog']" class='dog-icon' />
        <font-awesome-icon
          :icon="['fa-solid', 'fa-cat']" class='cat-icon'></font-awesome-icon>
      </div>
      <form class='form-card' @submit.prevent='submitFood'>
        <div class='field'>
          <label for='name'>Select your pet:</label>
          <select id='name' v-model='petName' required>
            <option v-for='pet in pets' :key='pet'>{{ pet }}</option>
          </select>
        </div>
        <div class='field'>
          <label for='food'>Enter food gram:</label>
          <input v-model='food' class='input' required type='number'>
        </div>
        <div class='field datepicker-field'>
          <label for='date'>Enter date and time:</label>
          <div style='padding-left: 10px'>
            <Datepicker v-model='date' :min-date='new Date()' class='datepicker-container' />
          </div>
        </div>
        <div class='field datepicker-field'>
          <label for='feeding-schedule'>Select feeding schedule:</label>
          <select id='feeding-schedule' v-model='feedingSchedule' required>
            <option value='once'>once</option>
            <option value='everyday'>every day</option>
            <option value='every week'>every week</option>
          </select>
        </div>
        <div class='field button_wrapper'>
          <BaseButton text='Add feeding' />
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.feeding-form {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.feeding-from-wrapper {
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

input, select {
  font-size: 30px;
  max-width: 300px;
  margin-left: 30px;
  border-radius: 5px;
  padding-left: 20px;
}

select {
  width: 300px;
}

.field {
  font-size: 40px;
  margin-bottom: 70px;
}

.datepicker-field {
  display: flex;
  align-items: center;
}

.datepicker-container {
  width: 250px;
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
