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
    <div
        v-for="(pet, index) in pets"
        v-if="pets.length > 0"
        :key="pet"
        class="pet-item"
    >
      <div class="pet-icon-container">
        <font-awesome-icon :icon="['fa-solid', 'fa-dog']" class="dog-icon"/>
        <font-awesome-icon :icon="['fa-solid', 'fa-cat']" class="dog-icon"/>
      </div>
      <div class="pet-container">
        <div class="pet-desc">Name: {{ pet.name }}</div>
        <div class="pet-desc">Weight: {{ pet.weight }} kg</div>
      </div>
      <div @click="deletePet(index)">
        <font-awesome-icon
            :icon="['fa-solid', 'fa-trash']"
            class="trash-icon"
        />
      </div>
    </div>
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

.pet-icon-container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.dog-icon {
  font-size: 70px;
  padding-left: 20px;
}

.pet-item {
  border-style: solid;
  border-radius: 10px;
  font-size: 40px;
  width: 600px;
  height: 130px;
  display: flex;
  flex-direction: row;
  margin: 20px;
}

.pet-desc {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pet-container {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.pet-list-empty {
  font-size: 30px;
}

.trash-icon {
  font-size: 30px;
  padding: 5px;
}

.trash-icon:hover {
  cursor: pointer;
}
</style>
