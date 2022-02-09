<template>
  <div>
    <el-row
      justify='space-between'
    >
      <h2>Add new recipe</h2>
    </el-row>
    <el-card
    >
      <recipe-form
        :errors='errors'
        :recipe='recipe'
        btn-label='Add recipe'
        @form-submit='handleSubmit'
      />
    </el-card>
  </div>
</template>

<script>
  import { QuillEditor } from '@vueup/vue-quill';
  import {
    ElCard,
    ElCol,
    ElForm,
    ElFormItem,
    ElInput,
    ElRow,
  } from 'element-plus';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { useStore } from 'vuex';
  import RecipeForm from './_includes/RecipeForm.vue';
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
      RecipeForm,
    },
    setup() {
      const store = useStore();
      const router = useRouter();

      let recipeObj = {
        title: '',
        portions: '',
        ingredients: '',
        steps: '',
        filters: [],
      };

      let recipe = ref({ ...recipeObj });
      let errors = ref({ ...recipeObj });

      const handleSubmit = (recipe) => {
        store.dispatch('recipe/add', recipe)
          .then(_ => {
            store.commit('global/dispatchToast', {
              type: 'success',
              title: 'Recipe addedd successfully!',
              description: '',
            });
            return router.push({
              name: 'admin.recipes.all',
              params: {
                reload: true,
              },
            });
          })
          .catch(err => {
            errors.value = err;
          });
      };

      return {
        recipe,
        errors,
        handleSubmit,
      };
    },
  };
</script>