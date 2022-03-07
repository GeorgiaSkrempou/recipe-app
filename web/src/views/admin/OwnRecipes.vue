<template>
  <div>
    <el-row
      align='middle'
      justify='space-between'
    >
      <div>
        <h2>Your recipes</h2>
      </div>
    </el-row>
    <el-row
      align='middle'
      class='mb-4'
      justify='space-between'
    >
      <el-col
        :span='4'
      >
        <el-input
          v-model='search'
          cleareable
          placeholder='Search a recipe'
        />
      </el-col>
      <router-link
        :to='{name: "admin.recipes.add"}'
        class='el-button el-button--primary el-button--small btn-link'
      >
        Add recipe
      </router-link>
    </el-row>
    <el-card>
      <el-table
        v-loading='loading'
        :data='visibleRecipes.filter((data) => !search || data.title.toLowerCase().includes(search.toLowerCase()))'
        @select='(r) => selectedRecipes.values = [...r]'
        @select-all='(r) => selectedRecipes.values = [...r]'
      >
        <el-table-column
          type='selection'
          width='55'
        />
        <el-table-column
          label='Title'
          prop='title'
        />
        <el-table-column
          label='Serves'
          prop='portions'
        />
        <el-table-column
          label='Tags'
          prop='filters'
        >
          <template #default='{ row }'>
            <el-check-tag
              v-for='filter in row.filters'
              :key='filter'
              :checked='isFilterChecked(filter)'
              class='mx-1'
              effect='dark'
              @change='handleFilterChange(filter)'
            >
              {{ filter }}
            </el-check-tag>
          </template>
        </el-table-column>
        <el-table-column
          align='right'
        >
          <template #header>
            <el-button
              v-if='selectedRecipes.values.length !== 0'
              size='small'
              type='primary'
              @click='handleRemoveRecipes'
            >
              Remove selected ({{ selectedRecipes.values.length }})
            </el-button>
          </template>
          <template #default='{ row }'>
            <div class='pt-2'>
              <router-link
                :to='{name: "admin.recipes.view", params: {id: row.id}}'
              >
                <el-tooltip
                  class='item'
                  content='View'
                  effect='light'
                  placement='top'
                >
                  <el-icon
                    class='me-2'
                  >
                    <icon-view />
                  </el-icon>
                </el-tooltip>
              </router-link>
              <router-link
                :to='{name: "admin.recipes.edit", params: {id: row.id}}'
              >
                <el-tooltip
                  class='item'
                  content='Edit'
                  effect='light'
                  placement='top'
                >
                  <el-icon
                    class='me-2'
                  >
                    <icon-edit />
                  </el-icon>
                </el-tooltip>
              </router-link>
              <el-tooltip
                class='item'
                content='Delete'
                effect='light'
                placement='top'
                style='cursor: pointer'
              >
                <el-icon
                  :size='20'
                  @click='showDeleteModal = true; selectedRecipe = row'
                >
                  <icon-delete />
                </el-icon>
              </el-tooltip>
            </div>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
    <el-dialog
      v-model='showDeleteModal'
      destroy-on-close
      title='Delete recipe'
      width='20%'
    >
      Are you sure you want to delete the selected recipe?
      <template #footer>
      <span class='dialog-footer'>
        <el-button
          size='medium'
          @click='showDeleteModal = false'
        >
          Cancel
        </el-button>
        <el-button
          :loading='deletingRecipe'
          size='medium'
          type='danger'
          @click='handleDeleteRecipe'
        >
          Confirm
        </el-button>
      </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
  import {
    ElButton,
    ElCard,
    ElCheckTag,
    ElCol,
    ElDialog,
    ElIcon,
    ElInput,
    ElRow,
    ElTable,
    ElTableColumn,
    ElTooltip,
  } from 'element-plus';
  import {
    computed,
    onMounted,
    reactive,
    ref,
  } from 'vue';
  import {
    useRoute,
    useRouter,
  } from 'vue-router';
  import { useStore } from 'vuex';

  export default {
    name: 'OwnRecipes',
    components: {
      ElButton,
      ElCard,
      ElCheckTag,
      ElCol,
      ElDialog,
      ElIcon,
      ElInput,
      ElRow,
      ElTable,
      ElTableColumn,
      ElTooltip,
    },
    setup() {
      const store = useStore();
      const route = useRoute();
      const router = useRouter();

      let loading = ref(false);
      let selectedRecipes = reactive([]);
      let search = ref('');
      let showDeleteModal = ref(false);
      let selectedRecipe = ref({});
      let deletingRecipe = ref(false);

      let recipes = computed(() => store.getters['recipe/ownRecipes']);
      let visibleRecipes = ref([]);
      const handleLoadRecipes = () => {
        loading.value = true;

        store.dispatch('recipe/getOwn')
          .then(_ => {
            loading.value = false;

            if (route.query.hasOwnProperty('tag')) {
              visibleRecipes.value = recipes.value.filter(recipe => recipe.filters.includes(route.query.tag));
            } else {
              visibleRecipes.value = recipes.value;
            }
          });
      };
      onMounted(() => {
        handleLoadRecipes();
      });

      let isFilterChecked = (filter) => {
        return route.query.hasOwnProperty('tag') && route.query.tag === filter;
      };
      const handleFilterChange = (filter) => {
        if (isFilterChecked(filter)) {
          router.push({ query: {} });
          visibleRecipes.value = recipes.value;
          return;
        }
        router.push({ query: { tag: filter } });
        visibleRecipes.value = recipes.value.filter(recipe => recipe.filters.includes(filter));
      };
      const handleRemoveRecipes = () => {
        const promises = [];
        selectedRecipes.values.forEach(recipe => {
          promises.push(
            store.dispatch('recipe/removeFromAccount', { recipe: recipe.id }),
          );
        });

        Promise.allSettled(promises)
          .then(r => {
            let addedRecipesCount = r.filter(promise => promise.status === 'fulfilled').length;
            if (addedRecipesCount !== 0) {
              store.commit('global/dispatchToast', {
                type: 'success',
                title: `Successfully removed ${addedRecipesCount} recipe(s) to your account!`,
                description: '',
              });
              handleLoadRecipes();
            }
          });
      };
      const handleDeleteRecipe = () => {
        deletingRecipe.value = true;
        store.dispatch('recipe/delete', selectedRecipe.value)
          .then(_ => {
            store.commit('global/dispatchToast', {
              type: 'success',
              title: `Successfully removed "${selectedRecipe.value.title}"`,
              description: '',
            });
          })
          .catch(err => {
            store.commit('global/dispatchToast', {
              type: 'error',
              title: 'There was an error removing the selected recipe',
              description: '',
            });
          })
          .finally(_ => {
            selectedRecipe.value = {};
            showDeleteModal.value = false;
            handleLoadRecipes();
          });
      };

      return {
        loading,
        visibleRecipes,
        selectedRecipes,
        search,
        showDeleteModal,
        selectedRecipe,
        deletingRecipe,

        isFilterChecked,
        handleFilterChange,
        handleRemoveRecipes,
        handleDeleteRecipe,
      };
    },
  };
</script>