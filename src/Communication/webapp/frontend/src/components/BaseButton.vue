<script setup>
defineProps({
  text: String,
});
</script>

<template>
  <button @click="$emit('click')"> {{ text }}</button>
</template>

<style scoped>
</style>
