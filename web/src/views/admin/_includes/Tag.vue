<template>
  <div>
    <el-tag
      v-for='tag in dynamicTags'
      :key='tag'
      :disable-transitions='false'
      class='mx-1'
      closable
      @close='handleClose(tag)'
    >
      {{ tag }}
    </el-tag>
    <el-input
      v-if='inputVisible'
      ref='inputRef'
      v-model='inputValue'
      class='ml-1 w-25'
      size='small'
      @blur='handleInputConfirm'
      @keyup.enter='handleInputConfirm'
    >
    </el-input>
    <el-button
      v-else
      class='button-new-tag ml-1'
      size='small'
      @click='showInput'
    >
      + New Filter
    </el-button>
  </div>
</template>

<script>
  import {
    ElButton,
    ElInput,
    ElTag,
  } from 'element-plus';
  import {
    nextTick,
    ref,
  } from 'vue';

  export default {
    name: 'Tag',
    components: {
      ElTag,
      ElButton,
      ElInput,
    },
    props: {
      tags: {
        type: Array,
        default: () => [],
      },
    },
    setup(props) {
      const inputValue = ref('');
      const dynamicTags = ref(props.tags);
      const inputVisible = ref(false);
      const inputRef = ref(null);

      const handleClose = (tag) => {
        dynamicTags.value.splice(dynamicTags.value.indexOf(tag), 1);
      };

      const showInput = () => {
        inputVisible.value = true;
        nextTick(() => {
          inputRef.value.focus();
        });
      };

      const handleInputConfirm = () => {
        if (inputValue.value) {
          dynamicTags.value.push(inputValue.value);
        }
        inputVisible.value = false;
        inputValue.value = '';
      };

      return {
        inputValue,
        inputRef,
        inputVisible,
        dynamicTags,
        handleClose,
        showInput,
        handleInputConfirm,
      };
    },
  };
</script>