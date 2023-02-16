<script setup>
import {useStore} from 'vuex';
import {computed, defineEmits, ref, toRaw} from 'vue';
import {Timestamp} from 'firebase/firestore';

const store = useStore();
const pets = computed(() => store.getters.petNames);
const date = ref();
const petName = ref();
const food = ref();
const emit = defineEmits(['goto-feedhistory']);
const feedingSchedule = ref();
const feedings = computed(() => store.getters.feedings);
const time = [];

function convertDateToStamp(feeding) {
  return new Timestamp(feeding.date.seconds, feeding.date.nanoseconds)
      .toDate()
      .getTime();
}

function submitFood() {
  let feedingArray = toRaw(this.feedings);
  let feedingForSubmitPet = feedingArray.filter(
      (feeding) => feeding.pet === this.petName
  );
  if (feedingForSubmitPet.length > 0) {
    const hasClosedFeedings = feedingForSubmitPet.filter(
        (feeding) =>
            Math.abs(convertDateToStamp(feeding) - this.date.getTime()) / 1000 < 120
    )
    if (hasClosedFeedings.length) {
      window.alert('Feeding time is too close to another one. Select a different time')
      return;
    }
  }
  store.dispatch('addFeeding', {
    petName,
    food,
    date,
    feedingSchedule,
  });
  emit('goto-feedhistory');
}
</script>

<template>
  <div class="form-wrapper">
    <div class="icons">
      <font-awesome-icon :icon="['fa-solid', 'fa-dog']" class="dog-icon"/>
      <font-awesome-icon :icon="['fa-solid', 'fa-cat']"/>
    </div>
    <div>
      <v-sheet width="500">
        <v-from @submit.prevent="submitFood">
          <v-select
              v-model="petName"
              :items="pets"
              aria-required="true"
              clearable
              density="compact"
              label="Select your pet"
          >
          </v-select>
          <v-text-field
              v-model="food"
              aria-required="true"
              label="Pet's food in grams"
              min="0"
              single-line
              type="number"
          />
          <label for="date">Enter date and time:</label>
          <Datepicker
              v-model="date"
              :min-date="new Date()"
              now-button-label="Current"
          />
          <v-select
              v-model="feedingSchedule"
              :items="['once', 'every day', 'every week']"
              aria-required="true"
              clearable
              density="compact"
              label="Select feeding schedule"
              style="padding-top: 20px"
          ></v-select>
          <v-btn block type="submit" @click="submitFood()">Submit</v-btn>
        </v-from>
      </v-sheet>
    </div>
  </div>
</template>

<style scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  opacity: 1;
}

.icons {
  font-size: xxx-large;
  margin-bottom: 20px;
}

.dog-icon {
  padding-right: 10px;
}
</style>
