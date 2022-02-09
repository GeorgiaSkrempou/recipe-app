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
          placeholder='Search a recipe'
          cleareable
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
      </el-table>
    </el-card>
  </div>
</template>

<script>
  import {
    ElCheckTag,
    ElInput,
    ElTable,
    ElTableColumn,
    ElRow,
    ElCol,
    ElCard,
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
      ElTable,
      ElTableColumn,
      ElCheckTag,
      ElInput,
      ElRow,
      ElCol,
      ElCard,
    },
    setup() {
      const store = useStore();
      const route = useRoute();
      const router = useRouter();

      let loading = ref(false);
      let selectedRecipes = reactive([]);
      let search = ref('');

      let recipes = computed(() => store.getters['recipe/ownRecipes']);
      let visibleRecipes = ref([]);
      onMounted(() => {
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

      return {
        loading,
        visibleRecipes,
        selectedRecipes,
        search,

        isFilterChecked,
        handleFilterChange,
      };
    },
  };
</script>