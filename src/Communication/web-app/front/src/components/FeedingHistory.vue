<script setup>
import { useStore } from 'vuex';
import { computed } from 'vue';

const store = useStore();
const feedings = computed(() => store.getters.feedings);

function getFormattedDate(date, schedule) {
  const dateObject = new Date((date.seconds + date.nanoseconds / 1e9) * 1000);
  if (schedule === 'once') {
    return `${dateObject.toLocaleDateString()} ${dateObject.toLocaleTimeString()}`;
  }
  return `${dateObject.toLocaleDateString('en-US', { weekday: 'long' })} ${dateObject.toLocaleTimeString()}`;
}

function deleteFeeding(index) {
  store.dispatch('deleteFeeding', { index });
}
</script>

<template>
  <div class='feeding-history'>
    <table>
      <thead>
      <tr>
        <th>Pet name</th>
        <th>Food quantity</th>
        <th>Feeding date</th>
        <th>Feeding schedule</th>
        <th></th>
      </tr>
      </thead>
      <tbody>
      <tr v-for='(feeding, index) in feedings' :key='feeding'>
        <td>{{ feeding.pet }}</td>
        <td>{{ feeding.food }}</td>
        <td>
          {{ getFormattedDate(feeding.date, feeding.schedule) }}
        </td>
        <td>{{ feeding.schedule }}</td>
        <td>
          <font-awesome-icon
              :icon="['fa-solid', 'fa-trash']"
              class='trash-icon'
              @click='deleteFeeding(index)'
          />
        </td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.feeding-history {
  padding: 100px;
  font-size: 20px;
}

table {
  border-collapse: separate;
  border: solid black 1px;
  border-radius: 6px;
  width: 100%;
}

td,
th {
  border-left: solid black 1px;
  border-top: solid black 1px;
  text-align: center;
  padding: 10px;
}

th {
  background-color: lightgray;
  border-top: none;
}

td:first-child,
th:first-child {
  border-left: none;
}

.trash-icon:hover {
  cursor: pointer;
}
</style>
