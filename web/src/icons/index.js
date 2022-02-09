import {
  View,
  Edit,
  Delete,
} from '@element-plus/icons';

export const loadIcons = (app) => {
  app.component('icon-view', View);
  app.component('icon-edit', Edit);
  app.component('icon-delete', Delete);
}