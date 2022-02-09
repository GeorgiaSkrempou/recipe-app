<template>
  <el-container style='background-color: #fff2f238' class='min-vh-100'>
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