<script setup>
import {useRouter} from 'vue-router';

const router = useRouter();

function changeRoute(url) {
  router.push(url);
}
</script>

<template>
  <div>
    <div class='img'></div>
    <div class='center'>
      <v-avatar size="100" style="margin: 25px"><img alt="logo" class="logo" src="../assets/iFeedLogo.png"></v-avatar>
      <div class='title'>iFeed</div>
      <div class='sub_title'>a site for pet feeding</div>
      <button class="commercial" @click="changeRoute('/commercial')">View our commercial  site</button>
      <div class='btns'>
        <button @click="changeRoute('/login')">Login</button>
        <button @click="changeRoute('/register')">Register</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.logo {
  height: 100px;
  width: 100px;
}

.img {
  width: 100%;
  height: 100vh;
  background-size: cover;
  background: url("../assets/dogCatEating.png") repeat;
  position: relative;
}

.img::before {
  content: "";
  position: absolute;
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.4);
}

.center {
  position: absolute;
  top: 52%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  padding: 0 20px;
  text-align: center;
  z-index: 2;
}

.center .title {
  color: #fff;
  font-size: 55px;
  font-weight: 600;
}

.center .sub_title {
  color: #fff;
  padding-top: 40px;
  font-size: 52px;
  font-weight: 600;
}

.center .commercial {
  height: 55px;
  width: 13em;
  border-radius: 5px;
  margin-top: 2em;
  border: 2px solid white;
  font-size: 20px;
  font-weight: 500;
  padding: 0 10px;
  cursor: pointer;
  outline: none;
  transition: all 0.3s ease;
  color: #fff;
  background: none;
}

.commercial:hover {
  background: white;
  color: black;
}

.center .btns {
  margin-top: 40px;
}

.center .btns button {
  height: 55px;
  width: 170px;
  border-radius: 5px;
  margin: 0 10px;
  border: 2px solid white;
  font-size: 20px;
  font-weight: 500;
  padding: 0 10px;
  cursor: pointer;
  outline: none;
  transition: all 0.3s ease;
}

.center .btns button:first-child {
  color: #fff;
  background: none;
}

.btns button:first-child:hover {
  background: white;
  color: black;
}

.center .btns button:last-child {
  background: white;
  color: black;
}
</style>
