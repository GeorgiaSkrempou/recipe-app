<template>
  <div>
    <el-row
      justify='space-between'
    >
      <h2>Add new recipe</h2>
    </el-row>
    <el-card
    >
      <el-form
        label-position='left'
      >
        <el-form-item
          :error='errors.title'
          label='Title'
          label-width='200px'
          required
        >
          <el-col
            :span='24'
            class='w-75'
          >
            <el-input
              v-model='recipe.title'
            />
          </el-col>
        </el-form-item>
        <el-form-item
          :error='errors.portions'
          label='Portions'
          label-width='200px'
          required
        >
          <el-col
            :span='24'
            class='w-75'
          >
            <el-input
              v-model='recipe.portions'
            />
          </el-col>
        </el-form-item>
        <el-form-item
          :error='errors.ingredients'
          label='Ingredients'
          label-width='200px'
          required
        >
          <el-col
            :span='24'
            class='w-75'
          >
            <quill-editor
              v-model='recipe.ingredients'
              theme='snow'
            />
          </el-col>
        </el-form-item>
        <el-form-item
          :error='errors.steps'
          label='Preparation steps'
          label-width='200px'
          required
        >
          <el-col
            :span='24'
            class='w-75'
          >
            <quill-editor
              v-model='recipe.steps'
              theme='snow'
            />
          </el-col>
        </el-form-item>
        <el-form-item
          :error='errors.steps'
          label='Filters'
          label-width='200px'
          required
        >
          <el-col
            :span='24'
            class='w-75'
          >
            <tag
              :tags='recipe.filters'
            />
          </el-col>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
  import {
    ElCard,
    ElForm,
    ElRow,
    ElFormItem,
    ElCol,
    ElInput,
  } from 'element-plus';
  import { ref } from 'vue';
  import { QuillEditor } from '@vueup/vue-quill';
  import Tag from './_includes/Tag.vue';

  export default {
    name: 'RecipeAdd',
    components: {
      ElRow,
      ElCard,
      ElForm,
      ElFormItem,
      ElCol,
      ElInput,
      QuillEditor,
      Tag,
    },
    setup() {
      let recipeObj = {
        title: '',
        portions: '',
        ingredients: '',
        steps: '',
        filters: [],
      };

      let recipe = ref({ ...recipeObj });
      let errors = ref({ ...recipeObj });

      return {
        recipe,
        errors,
      };
    },
  };
</script>