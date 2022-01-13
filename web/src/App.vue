<template>
  <el-container style='background-color: var(--el-bg-color-base)' class='min-vh-100'>
    <router-view />
  </el-container>
</template>

<script>
  import {
    ElContainer,
    ElMain,
  } from 'element-plus';

  export default {
    components: {
      ElContainer,
      ElMain,
    },
  };
</script>