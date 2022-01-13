<template>
  <div>
    <el-container>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </div>
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