<template>
  <div class='home' />
</template>

<script>
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';

  export default {
    name: 'Home',
    setup() {
      onMounted(() => {
        useRouter().push({ name: 'public.login' });
      });
    },
  };
</script>
