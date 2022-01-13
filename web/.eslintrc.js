module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/recommended',
  ],
  rules: {
    'vue/html-closing-bracket-newline': 'off',
    'comma-dangle': ['error', 'always-multiline'],
    'semi': ['error', 'always'],
    'vue/script-indent': ['error', 2, {
      'baseIndent': 1,
      'switchCase': 1,
    }],
    'vue/html-quotes': ['error', 'single', { 'avoidEscape': true }],
    'handle-callback-err': 'off',
    'vue/order-in-components': ['error'],
    'vue/no-v-html': 'off',
  },
  'overrides': [
    {
      'files': ['*.vue'],
      'rules': {
        'indent': 'off',
      },
    },
  ],
  parserOptions: {
    'parser': 'babel-eslint',
    'sourceType': 'module',
  },
};
