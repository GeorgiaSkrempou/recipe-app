<template>
  <el-row justify='center'>
    <el-card>
      <el-alert
        v-if='showError'
        :closable='false'
        show-icon
        title='Email or password incorrect'
        type='error'
      />
      <el-form>
        <h4 style='font-size: var(--el-font-size-medium)'>
          Login
        </h4>
        <el-form-item>
          <el-input
            v-model='userEmail'
            :prefix-icon='userIcon'
          />
        </el-form-item>
        <el-form-item>
          <el-input
            v-model='userPassword'
            :prefix-icon='pwdIcon'
            show-password
          />
        </el-form-item>
        <el-form-item>
          <el-button
            :loading='loading'
            type='primary'
            @click='handleLogin'
          >
            Login
          </el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </el-row>
</template>

<script>
  import {
    Lock,
    User,
  } from '@element-plus/icons';
  import {
    ElAlert,
    ElButton,
    ElCard,
    ElForm,
    ElFormItem,
    ElInput,
    ElRow,
  } from 'element-plus';

  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { useStore } from 'vuex';

  export default {
    components: {
      ElInput,
      ElButton,
      ElForm,
      ElCard,
      ElRow,
      ElFormItem,
      ElAlert,
    },
    setup() {
      const store = useStore();
      const router = useRouter();

      let email = ref('');
      let password = ref('');
      let loading = ref(false);
      let showError = ref(false);

      const handleLogin = () => {
        loading.value = true;
        store.dispatch('user/login', { email: email.value, password: password.value })
          .then(_ => {
            router.push({ name: 'admin.recipes' });
          })
          .catch(err => {
            showError.value = true;
          })
          .finally(_ => {
            loading.value = false;
          });
      };

      return {
        userEmail: email,
        userPassword: password,
        userIcon: User,
        pwdIcon: Lock,
        showError: showError,
        loading,

        handleLogin,
      };
    },
  };
</script>