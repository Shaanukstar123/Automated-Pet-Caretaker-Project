<script setup>
import {ref} from 'vue';
import {useStore} from 'vuex';

const emit = defineEmits(['return-home']);

const name = ref();
const weight = ref();
const store = useStore();

function submitPet() {
  store.dispatch('addPet', {name, weight});
  emit('return-home');
}
</script>

<template>
  <div class="form-wrapper">
    <div class="icons">
      <font-awesome-icon :icon="['fa-solid', 'fa-dog']" class='dog-icon'/>
      <font-awesome-icon :icon="['fa-solid', 'fa-cat']"/>
    </div>
    <div>
      <v-sheet width="500">
        <v-from @submit.prevent="submitPet">
          <v-text-field
              v-model="name"
              aria-required="true"
              label="Pet's name"
          >
          </v-text-field>
          <v-text-field
              v-model="weight"
              aria-required="true"
              label="Pet's weight (kg)"
              min="0"
              single-line
              type="number"
          />
          <v-btn block type="submit" @click="submitPet()">Submit</v-btn>
        </v-from>
      </v-sheet>
    </div>
  </div>
</template>

<style scoped>

.icons {
  font-size: xxx-large;
  margin-bottom: 20px;
}

.form-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  opacity: 1;
}

.dog-icon {
  padding-right: 10px;
}

</style>
