const fs = require('fs');

let configFile = 'src/config/config.js';
if (process.env.APP_ENV === 'dev') {
  fs.copyFileSync('src/config/config.dev.js', configFile);
} else {
  fs.copyFileSync('src/config/config.prod.js', configFile);
}