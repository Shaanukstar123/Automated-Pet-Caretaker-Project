import { getFirestore } from 'firebase/firestore';
import { initializeApp } from 'firebase/app';

const firebaseConfig = {
  apiKey: 'AIzaSyBMwXjn_S0khDUBodg7pwLsK9vuOQJJNJE',
  authDomain: 'auth-dogs.firebaseapp.com',
  projectId: 'auth-dogs',
  storageBucket: 'auth-dogs.appspot.com',
  messagingSenderId: '314481891127',
  appId: '1:314481891127:web:66c7af5df81cb4c0feecb2',
};

initializeApp(firebaseConfig);

export const db = getFirestore();
