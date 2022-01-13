<template>
  <div class='sidebar'>
    <el-menu
      :default-active='computeActiveMenuItem'
      :router='true'
      active-text-color='#fff'
      background-color='#4f5d73'
      class='border-0'
      text-color='#9da5b1'
    >
      <el-menu-item
        v-for='(menu, key) in menuItems'
        :key='key'
        :index='key.toString()'
        :route='{name: menu.route}'
      >
        <el-icon
          :size='20'
        >
          <component
            :is='menu.icon'
            class='me-2'
          />
        </el-icon>
        {{ menu.name }}
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
  import {
    ElIcon,
    ElMenu,
    ElMenuItem,
  } from 'element-plus';
  import { computed } from 'vue';
  import { useRoute } from 'vue-router';

  export default {
    name: 'Sidebar',
    components: {
      ElMenu,
      ElMenuItem,
      ElIcon,
    },
    setup() {
      const route = useRoute();
      const menuItems = [
        {
          name: 'Dashboard',
          icon: 'icon-home',
          route: 'admin.home',
        }, {
          name: 'Recipes',
          icon: 'icon-server',
          route: 'admin.recipes',
        },
      ];
      const parseRoute = (route) => {
        let splitRoute = route.split('.');
        return [splitRoute[0], splitRoute[1]].join('.');
      };
      let computeActiveMenuItem = computed(() => {
        return menuItems.findIndex((el) => parseRoute(el.route) === parseRoute(route.name)).toString();
      });
      return {
        menuItems,
        computeActiveMenuItem,
      };
    },
  };
</script>