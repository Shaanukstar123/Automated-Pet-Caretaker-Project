import { createStore } from 'vuex';
import {
  createUserWithEmailAndPassword,
  getAuth,
  signInWithEmailAndPassword,
  signOut,
} from 'firebase/auth';
import {
  addDoc,
  collection,
  deleteDoc,
  doc,
  getDocs,
} from 'firebase/firestore';
import { db } from '../firebase';

const store = createStore({
  state: {
    user: {
      loggedIn: false,
      data: null,
    },
    pets: [],
    feedings: [],
  },
  getters: {
    user(state) {
      return state.user;
    },
    pets(state) {
      return state.pets;
    },
    petNames(state) {
      return state.pets.map((pet) => pet.name);
    },
    feedings(state) {
      return state.feedings;
    },
  },
  mutations: {
    SET_LOGGED_IN(state, value) {
      state.user.loggedIn = value;
    },
    SET_USER(state, data) {
      state.user.data = data;
    },
    SET_PETS(state, data) {
      state.pets = data;
    },
    SET_FEEDINGS(state, data) {
      state.feedings = data;
    },
    UPDATE_FEEDINGS(state, data) {
      data.date = {
        seconds: Math.floor(data.date.getTime() / 1000),
        nanoseconds: (data.date.getTime() % 1000) * 1e9,
      };
      state.feedings.push(data);
    },
    UPDATE_PETS(state, data) {
      state.pets.push(data);
    },
    DELETE_PET(state, index) {
      state.pets.splice(index, 1);
    },
    DELETE_FEEDING(state, index) {
      state.feedings.splice(index, 1);
    },
  },
  actions: {
    register(context, { email, password }) {
      return createUserWithEmailAndPassword(getAuth(), email, password)
        .then((response) => {
          if (response) {
            context.commit('SET_USER', response.user);
            context.commit('SET_LOGGED_IN', true);
          }
        })
        .catch((error) => Promise.reject(error));
    },

    logIn(context, { email, password }) {
      return signInWithEmailAndPassword(getAuth(), email, password)
        .then((response) => {
          if (response) {
            context.commit('SET_USER', response.user);
            context.commit('SET_LOGGED_IN', true);
          }
        })
        .then(() => {
          context.dispatch('fetchPets');
          context.dispatch('fetchFeedings');
        })
        .catch((error) => Promise.reject(error));
    },

    async logOut(context) {
      await signOut(getAuth());
      context.commit('SET_USER', null);
      context.commit('SET_LOGGED_IN', false);
      context.commit('SET_PETS', []);
    },

    async fetchPets(context) {
      // Change the firestore collection mae
      const petsRef = collection(db, 'pets');
      const user = context.state.user.data;
      const snapshot = await getDocs(petsRef);
      const pets = snapshot.docs.map((doc) => ({
        ...doc.data(),
        id: doc.id,
      }));
      // filter with based on owner email
      const userPets = pets.filter((pet) => pet.owner === user.email);
      context.commit('SET_PETS', userPets);
    },
    async fetchFeedings(context) {
      const feedingRef = collection(db, 'feedings');
      const user = context.state.user.data;
      const snapshot = await getDocs(feedingRef);
      const feedings = snapshot.docs.map((doc) => ({
        ...doc.data(),
        id: doc.id,
      }));
      const userFeedings = feedings.filter((pet) => pet.owner === user.email);
      context.commit('SET_FEEDINGS', userFeedings);
    },

    addPet(context, { name, weight }) {
      const { email } = context.state.user.data;
      const pet = { name: name.value, owner: email, weight: weight.value };
      addDoc(collection(db, 'pets'), {
        name: pet.name,
        owner: pet.owner,
        weight: pet.weight,
      }).then((response) => {
        pet.id = response.id;
        context.commit('UPDATE_PETS', pet);
      });
    },
    addFeeding(context, { petName, food, date, feedingSchedule }) {
      const { email } = context.state.user.data;
      const feeding = {
        date: new Date(date.value),
        pet: petName.value,
        food: food.value,
        owner: email,
        schedule: feedingSchedule.value,
      };
      addDoc(collection(db, 'feedings'), {
        date: feeding.date,
        pet: feeding.pet,
        food: feeding.food,
        owner: feeding.owner,
        schedule: feeding.schedule,
      }).then((response) => {
        feeding.id = response.id;
        context.commit('UPDATE_FEEDINGS', feeding);
        context.dispatch('sendFeeding', feeding);
      });
    },
    deletePet(context, { index }) {
      const pet = context.getters.pets[index];
      deleteDoc(doc(db, 'pets', pet.id)).then(() => {
        context.commit('DELETE_PET', index);
      });
    },
    deleteFeeding(context, { index }) {
      const feeding = context.getters.feedings[index];
      deleteDoc(doc(db, 'feedings', feeding.id)).then(() => {
        context.commit('DELETE_FEEDING', index);
        context.dispatch('deleteRemoteFeeding', feeding)
      });
    },
    sendFeeding(context, feeding) {
      let feedingObject = { ...feeding };
      feedingObject.date = new Date(
        feedingObject.date.seconds * 1000
      ).toLocaleString('default', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      });
      fetch('http://127.0.0.1:8000', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(feedingObject),
      })
        .then((response) => response.json())
        .catch((error) => console.error(error));
    },
    deleteRemoteFeeding(context, feeding) {
      let feedingObject = { ...feeding };
      feedingObject.date = new Date(
        feedingObject.date.seconds * 1000
      ).toLocaleString('default', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
      });
      fetch('http://127.0.0.1:8000', {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(feedingObject),
      })
        .then((response) => response.json())
        .catch((error) => console.error(error));
    },
  },
});

// export the store
export default store;
