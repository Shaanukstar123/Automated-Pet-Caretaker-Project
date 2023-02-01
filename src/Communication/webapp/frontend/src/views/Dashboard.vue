<script setup>
import { useStore } from 'vuex';
import { computed, ref } from 'vue';
import BaseButton from '../components/BaseButton.vue';
import PetList from '../components/PetList.vue';
import router from '../routes/index.js';
import CreatePet from '../components/CreatePet.vue';
import FeedingHistory from '../components/FeedingHistory.vue';
import FeedingForm from '../components/FeedingForm.vue';

const store = useStore();
const email = computed(() => store.getters.user.data.email);
const activeTabIndex = ref(0);

function logout() {
  store.dispatch('logOut').then(() => router.push('/'));
}
</script>

<template>
  <div class="dashboard">
    <div class="navbar">
      <div class="navbar__wrapper">
        <font-awesome-icon
            :icon="['fa-solid', 'fa-user']"
            class="navbar__user"
        />
        <div class="navbar__item navbar__email">{{ email }}</div>
        <div class="navbar__action">
          <BaseButton
              class="navbar__item"
              text="My pets"
              @click="activeTabIndex = 0"
          />
          <BaseButton
              class="navbar__item"
              text="Add pet"
              @click="activeTabIndex = 1"
          />
          <BaseButton
              class="navbar__item"
              text="Add feeding time"
              @click="activeTabIndex = 2"
          />
          <BaseButton
              class="navbar__item"
              text="Feeding history"
              @click="activeTabIndex = 3"
          />
        </div>
      </div>
      <BaseButton class="navbar__item" text="Logout" @click="logout"/>
    </div>
    <div class="content">
      <div v-if="activeTabIndex === 0" class="content__item">
        <span class="content__title">My pets</span>
        <PetList/>
      </div>
      <div v-if="activeTabIndex === 1" class="content__item">
        <span class="content__title">Add a new pet</span>
        <CreatePet @return-home="activeTabIndex = 0"/>
      </div>
      <div v-if="activeTabIndex === 2" class="content__item">
        <span class="content__title">Add feeding </span>
        <FeedingForm @goto-feedhistory="activeTabIndex=3"></FeedingForm>
      </div>
      <div v-if='activeTabIndex === 3' class='content__item'>
        <span class='content__title'>Feeding history</span>
        <FeedingHistory/>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  display: flex;
  flex-direction: row;
  width: 100%;
  height: 100%;
  margin: 2em 1em;
}

.navbar__user {
  font-size: 100px;
}

.navbar {
  width: 20%;
  height: 95vh;
  display: flex;
  flex-direction: column;
  font-size: 30px;
}

.navbar__item {
  margin: 1em 0;
  font-size: 30px;
  padding: 10px;
  border-radius: 10px;
}

.navbar__wrapper {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.navbar__action {
  margin: 3em 0;
  display: flex;
  flex-direction: column;
}

.navbar__email {
  font-size: 20px;
}

.content {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content__item {
  width: 100%;
  height: 100%;
}

.content__title {
  font-size: 40px;
  display: flex;
  justify-content: center;
}
</style>
