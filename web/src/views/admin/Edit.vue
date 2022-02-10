<template>
  <div>
    <el-row
      justify='space-between'
    >
      <h2>Edit recipe</h2>
    </el-row>
    <el-card
    >
      <recipe-form
        :errors='errors'
        :recipe='recipe'
        :loading='loading'
        :updating='updating'
        btn-label='Edit recipe'
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
  import {
    computed,
    onMounted,
    ref,
  } from 'vue';
  import {
    onBeforeRouteLeave,
    useRoute,
    useRouter,
  } from 'vue-router';
  import { useStore } from 'vuex';
  import RecipeForm from './_includes/RecipeForm.vue';
  import Tag from './_includes/Tag.vue';

  export default {
    name: 'RecipeAdd',
    components: {
      ElCard,
      ElCol,
      ElForm,
      ElFormItem,
      ElInput,
      ElRow,

      QuillEditor,
      Tag,
      RecipeForm,
    },
    setup() {
      const store = useStore();
      const router = useRouter();
      const route = useRoute();

      let recipeObj = {
        title: '',
        portions: '',
        ingredients: '',
        steps: '',
        filters: [],
      };

      let recipe = computed(() => store.getters['recipe/recipe']);
      let errors = ref({ ...recipeObj });
      let loading = ref(false);
      let updating = ref(false);

      onMounted(() => {
        loading.value = true;
        store.dispatch('recipe/getRecipe', route.params.id)
          .then(_ => {
            loading.value = false;
          })
      });
      onBeforeRouteLeave(() => {
        store.commit('recipe/setRecipe', recipeObj);
      })

      const handleSubmit = (recipe) => {
        updating.value = true;
        store.dispatch('recipe/update', recipe)
          .then(_ => {
            store.commit('global/dispatchToast', {
              type: 'success',
              title: 'Recipe updated successfully!',
              description: '',
            });
            updating.value = false;
          })
          .catch(err => {
            updating.value = false;
            errors.value = err;
          });
      };

      return {
        recipe,
        errors,
        loading,
        updating,

        handleSubmit,
      };
    },
  };
</script>