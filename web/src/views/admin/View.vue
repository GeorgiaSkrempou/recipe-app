<template>
  <div>
    <el-row
      justify='space-between'
    >
      <h2>Recipe details</h2>
    </el-row>
    <el-card
      v-loading='loading'
    >
      <el-row>
        <el-col
          :span='4'
          class='text-muted'
        >
          Title
        </el-col>
        <el-col
          :span='20'
        >
          {{ recipe.title }}
        </el-col>
      </el-row>
      <el-divider />
      <el-row>
        <el-col
          :span='4'
          class='text-muted'
        >
          Portions
        </el-col>
        <el-col
          :span='20'
        >
          {{ recipe.portions }}
        </el-col>
      </el-row>
      <el-divider />
      <el-row>
        <el-col
          :span='4'
          class='text-muted'
        >
          Ingredients
        </el-col>
        <el-col
          :span='20'
        >
          <div v-html='recipe.ingredients' />
        </el-col>
      </el-row>
      <el-divider />
      <el-row>
        <el-col
          :span='4'
          class='text-muted'
        >
          Steps
        </el-col>
        <el-col
          :span='20'
        >
          <div v-html='recipe.steps' />
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script>
  import { QuillEditor } from '@vueup/vue-quill';
  import {
    ElCard,
    ElCol,
    ElDivider,
    ElForm,
    ElFormItem,
    ElInput,
    ElRow,
  } from 'element-plus';
  import {
    computed,
    onMounted,
    ref,
  } from 'vue';
  import { useRoute } from 'vue-router';
  import { useStore } from 'vuex';
  import Tag from './_includes/Tag.vue';

  export default {
    name: 'RecipeView',
    components: {
      ElCard,
      ElCol,
      ElDivider,
      ElForm,
      ElFormItem,
      ElInput,
      ElRow,

      QuillEditor,
      Tag,
    },
    setup() {
      const store = useStore();
      const route = useRoute();

      let loading = ref(false);

      let recipe = computed(() => store.getters['recipe/recipe']);
      onMounted(() => {
        loading.value = true;
        store.dispatch('recipe/getRecipe', route.params.id)
          .then(_ => {
            loading.value = false;
          });
      });
      return {
        loading,
        recipe,
      };
    },
  };
</script>