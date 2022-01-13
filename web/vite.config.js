import vue from '@vitejs/plugin-vue';
import path from 'path';
import { defineConfig } from 'vite';
import fs from 'fs';

let configFile = 'src/config/config.js';
if (process.env.APP_ENV === 'dev') {
  fs.copyFileSync('src/config/config.dev.js', configFile);
} else {
  fs.copyFileSync('src/config/config.prod.js', configFile);
}

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@/': `${path.resolve(__dirname, 'src')}/`,
    },
  },
});