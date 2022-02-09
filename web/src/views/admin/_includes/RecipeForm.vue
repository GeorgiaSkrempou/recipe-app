<template>
  <el-form
    v-loading='loading'
    label-position='left'
    status-icon
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
          v-model:content='recipe.ingredients'
          content-type='html'
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
          v-model:content='recipe.steps'
          content-type='html'
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
    <el-form-item
      class='mb-0'
    >
      <el-button
        size='medium'
        style='float: right;'
        type='primary'
        @click='$emit("form-submit", recipe)'
      >
        {{ btnLabel }}
      </el-button>
    </el-form-item>
  </el-form>
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
    ElButton,
  } from 'element-plus';
  import Tag from './Tag.vue';

  export default {
    components: {
      ElRow,
      ElCard,
      ElForm,
      ElFormItem,
      ElCol,
      ElInput,
      ElButton,

      QuillEditor,
      Tag,
    },
    props: {
      recipe: {
        type: Object,
        required: true,
      },
      errors: {
        type: Object,
        required: true,
      },
      loading: {
        type: Boolean,
        required: false,
      },
      btnLabel: {
        type: String,
        required: true,
      },
    },
  };
</script>