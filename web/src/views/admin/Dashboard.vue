<template>
  <div>
    <el-row justify='center'>
      <el-col :xl='12'>
        <router-view />
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import {
    ElCol,
    ElRow,
  } from 'element-plus';

  export default {
    components: {
      ElRow,
      ElCol,
    },
  };
</script>