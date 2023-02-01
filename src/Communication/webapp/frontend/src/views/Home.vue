<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

function changeRoute(url) {
  router.push(url);
}
</script>

<template>
  <div>
    <div class='img'></div>
    <div class='center'>
      <div class='title'>Pet Feeding App</div>
      <div class='sub_title'>a site for pet feeding</div>
      <div class='btns'>
        <button @click="changeRoute('/login')">Login</button>
        <button @click="changeRoute('/register')">Register</button>
      </div>
    </div>
  </div>
</template>

<style scoped>

.img {
  background: url("../assets/dogs.jpg") no-repeat;
  width: 100%;
  height: 100vh;
  background-size: cover;
  background-position: center;
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
