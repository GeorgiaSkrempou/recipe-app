<template>
  <el-form
    v-if='loading === false'
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
          :content='recipe.ingredients'
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
          :content='recipe.steps'
          content-type='html'
          theme='snow'
        />
      </el-col>
    </el-form-item>
    <el-form-item
      label='Image'
      label-width='200px'
    >
      <el-col
        :span='24'
        class='w-75'
      >
        <file-upload
          :files='recipe.image'
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
        :loading='updating'
        class='btn-link'
        @click='$emit("form-submit", recipe)'
      >
        {{ btnLabel }}
      </el-button>
    </el-form-item>
  </el-form>
  <div
    v-else
    class='m-auto'
    style='width: 1px;'
  >
    <el-icon
      class='loading-data is-loading'
    >
      <icon-loading />
    </el-icon>
  </div>
</template>

<script>
  import { QuillEditor } from '@vueup/vue-quill';
  import {
    ElButton,
    ElCard,
    ElCol,
    ElForm,
    ElFormItem,
    ElIcon,
    ElInput,
    ElRow,
  } from 'element-plus';
  import Tag from './Tag.vue';
  import FileUpload from './FileUpload.vue';

  export default {
    components: {
      ElRow,
      ElCard,
      ElForm,
      ElFormItem,
      ElIcon,
      ElCol,
      ElInput,
      ElButton,

      FileUpload,
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
      updating: {
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