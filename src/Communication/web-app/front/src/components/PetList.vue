<script setup>
import { useStore } from 'vuex';
import { computed } from 'vue';

const store = useStore();
const pets = computed(() => store.getters.pets);

function deletePet(index) {
  store.dispatch('deletePet', { index });
}
</script>

<template>
  <div class="pet-list">
    <v-card
      v-for="(pet, index) in pets"
      v-if="pets.length > 0"
      :key="pet"
      variant="tonal"
    >
      <v-card-title>
        <div style="display: flex; flex-direction: column; justify-content: space-around">
          <div class="pet-icon-container">
            <font-awesome-icon
              :icon="['fa-solid', 'fa-dog']"
              class="dog-icon"
            />
            <font-awesome-icon
              :icon="['fa-solid', 'fa-cat']"
              class="dog-icon"
            />
          </div>
          <v-card-actions>
            <v-btn @click="deletePet(index)">Delete pet</v-btn>
          </v-card-actions>
        </div>
        <div class="pet-container">
          <div class="pet-desc" style='margin-bottom: 0.5em'>
            <div class="pet-desc-header">Name</div>
            <div>{{ pet.name }}</div>
          </div>
          <div class="pet-desc">
            <div class="pet-desc-header">Weight</div>
            <div>{{ pet.weight }} kg</div>
          </div>
        </div>
      </v-card-title>
    </v-card>
    <div v-else class="pet-list-empty">You haven't added any pets yet</div>
  </div>
</template>

<style scoped>
.pet-list {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
}

:deep(.v-card) {
  margin: 10px;
  border-radius: 1em;
}

:deep(.v-card-title) {
  padding: 0;
  display: flex;
}

.pet-icon-container {
  padding: 0.5em;
  display: flex;
  justify-content: center;
  align-items: center;
}

.dog-icon {
  font-size: 70px;
  padding-left: 20px;
}

.pet-desc {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.pet-desc-header {
  font-size: 20px;
  font-weight: bold;
}

.pet-container {
  background-color: #ddd;
  border: none;
  color: black;
  padding: 10px 30px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin-left: 1em;
  border-radius: 16px;
}

.pet-list-empty {
  font-size: 30px;
}
</style>
