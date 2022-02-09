<template>
  <el-container>
    <el-container>
      <el-aside>
        <sidebar />
      </el-aside>
      <el-main>
        <router-view v-slot='{ Component, route }'>
          <transition name='fade' mode='out-in'>
            <component :is='Component' :key='route.path' />
          </transition>
        </router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
  import {
    ElMain,
    ElAside,
    ElHeader,
    ElContainer,
  } from 'element-plus';

  import Sidebar from './_includes/Sidebar.vue';
  import Navbar from './_includes/Navbar.vue';

  export default {
    components: {
      ElMain,
      ElAside,
      ElHeader,
      ElContainer,

      Sidebar,
      Navbar,
    },
  };
</script>