<template>
  <el-row
    class='navbar'
    justify='space-between'
  >
    <div class='h-100'>
      <div class='navbar-brand text-center'>
        Recipes
      </div>
    </div>
    <div>
      <el-dropdown class='me-4'>
        <span class='el-dropdown-link'>
         <el-avatar src='https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png' />
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>Action 1</el-dropdown-item>
            <el-dropdown-item>Action 2</el-dropdown-item>
            <el-dropdown-item>Action 3</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </el-row>
</template>

<script>
  import {
    ElAvatar,
    ElDropdown,
    ElDropdownItem,
    ElDropdownMenu,
    ElMenu,
    ElMenuItem,
    ElRow,
  } from 'element-plus';

  export default {
    name: 'Navbar',
    components: {
      ElMenu,
      ElMenuItem,
      ElRow,
      ElDropdown,
      ElDropdownMenu,
      ElDropdownItem,
      ElAvatar,
    },
  };
</script>
