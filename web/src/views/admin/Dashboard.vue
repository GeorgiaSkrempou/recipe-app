<template>
  <el-container>
    <el-container>
      <el-aside>
        <sidebar />
      </el-aside>
      <el-main>
        <router-view v-slot='{ Component, route }'>
          <transition mode='out-in' name='fade'>
            <component :is='Component' :key='route.path' />
          </transition>
        </router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
  import {
    ElAside,
    ElContainer,
    ElHeader,
    ElMain,
  } from 'element-plus';
  import Navbar from './_includes/Navbar.vue';

  import Sidebar from './_includes/Sidebar.vue';

  export default {
    components: {
      ElAside,
      ElContainer,
      ElHeader,
      ElMain,

      Sidebar,
      Navbar,
    },
  };
</script>