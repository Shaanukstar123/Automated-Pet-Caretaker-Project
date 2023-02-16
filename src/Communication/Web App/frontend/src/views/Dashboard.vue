<script setup>
import {useStore} from 'vuex';
import {computed, ref} from 'vue';
import PetList from '../components/PetList.vue';
import router from '../routes/index.js';
import CreatePet from '../components/CreatePet.vue';
import FeedingHistory from '../components/FeedingHistory.vue';
import FeedingForm from '../components/FeedingForm.vue';
import LiveStream from "../components/LiveStream.vue";

const store = useStore();
const email = computed(() => store.getters.user.data.email);
const activeTabIndex = ref(0);

function logout() {
  store.dispatch('logOut').then(() => router.push('/'));
}
</script>

<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer
          floating
          permanent
      >
        <v-list
            density="compact"
            nav
        >
          <div class="logo">
            <img alt="logo" src="../assets/iFeed.png"/>
          </div>
          <v-list-item>
            <div class="email">
              <font-awesome-icon
                  :icon="['fa-solid', 'fa-user']"
                  class="navbar__user"/>
              <div style="padding-bottom: 7px;">{{ email }}</div>
            </div>
          </v-list-item>
          <div>
            <v-divider></v-divider>
          </div>

          <div class="nav-items">
            <v-list-item title="My pets" @click="activeTabIndex=0"></v-list-item>
            <v-list-item title="Add pet" @click="activeTabIndex=1"></v-list-item>
            <v-list-item title="Add feeding time" @click="activeTabIndex=2"></v-list-item>
            <v-list-item title="Feeding history" @click="activeTabIndex=3"></v-list-item>
            <v-list-item title="LiveStream" @click="activeTabIndex=4"></v-list-item>
          </div>
          <div class="logout-wrapper">
            <v-list-item class="logout" title="Logout" @click="logout">
            </v-list-item>
          </div>
        </v-list>
      </v-navigation-drawer>
      <v-main style="height: 100vh; background-color: #f5f7f8;">
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
          <div v-if='activeTabIndex === 4' class='content__item'>
            <span class='content__title'>Live Stream</span>
            <LiveStream/>
          </div>
        </div>
        <div class="content2">
        </div>
      </v-main>
    </v-layout>
  </v-card>
</template>

<style scoped>
.logo {
  display: flex;
  justify-content: center;

}

img {
  height: 150px;
}

.navbar__user {
  font-size: 25px;
  margin-top: 10px;
  padding-right: 20px;
}

:deep(.v-list) {
  height: 100%;
}

:deep(.v-layout) {
  background-color: #f5f7f8;
}

:deep(.v-navigation-drawer) {
  height: calc(100% - 60px) !important;
  border-radius: 21px;
  margin: 30px;
}

:deep(.v-list-item) {
  display: flex;
  justify-content: center;
  margin: 10px;
}

:deep(.v-list-item-title) {
  font-size: medium;
  line-height: 2rem;
}

:deep(.v-main) {
  background-color: rgb(245, 247, 248);
  display: flex;
  justify-content: center;
}

.nav-items {
  margin-top: 10px;
  font-size: large;
}

.email {
  margin-top: -10px;
  display: flex;
  align-items: baseline;
  justify-content: center;
  margin-bottom: 10px;
}

.logout-wrapper {
  display: flex;
  position: relative;
  height: 100%;
  text-align: end;
  align-content: flex-end;
  justify-content: center;
}

.logout {
  width: 100%;
  position: absolute;
  bottom: 480px;

}

.content {
  width: 80%;
  height: 78%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 5em;
  padding: 2em;
  background-color: white;
  border-radius: 10px;
  position: relative;
  z-index: 3;
  overflow-y: auto;
}

.content:before {
  content: "";
  position: absolute;
  z-index: -1;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: url("../assets/animalbg.jpg") center center;
  opacity: .03;
}

.content2 {
  width: 98%;
  height: 34vh;
  position: absolute;
  z-index: 1;
  background: url("/src/assets/photomain.png") center center;
  background-repeat: repeat;
  bottom: 0;
  margin-left: 332px;
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
