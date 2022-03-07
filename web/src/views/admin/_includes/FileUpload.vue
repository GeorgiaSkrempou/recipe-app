<template>
  <file-pond
    :allow-file-type-validation='false'
    :allow-multiple='false'
    credits='false'
    name='image'

    v-bind:files='files'
  />
</template>

<script>
  import FilePondPluginFileValidateType from 'filepond-plugin-file-validate-type';
  import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
  import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css';
  import 'filepond/dist/filepond.min.css';

  import vueFilePond from 'vue-filepond';

  const FilePond = vueFilePond(
    FilePondPluginImagePreview,
    FilePondPluginFileValidateType,
  );

  export default {
    name: 'FileUpload',
    components: {
      FilePond,
    },
    props: {
      files: {
        type: Array,
        default: () => [],
      },
    },
  };
</script>