https://play.vuejs.org/#eNp9kVFLwzAQx7  Hello World!
https://play.vuejs.org/#eNp9kk9r 组合式API count

```HTML
<!DOCTYPE html>
<html>

<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>JSFiddle 2ke1ab0z</title>

  <style>
    
  </style>

  
</head>
<body>
  <script type="importmap">
  {
    "imports": {
      "vue": "https://unpkg.com/vue@3/dist/vue.esm-browser.js"
    }
  }
</script>

<div id="app">{{ message }}</div>

<script type="module">
  import { createApp } from 'vue'

  createApp({
    data() {
      return {
        message: 'Hello Vue!'
      }
    }
  }).mount('#app')
</script>

  <script>
    
  </script>
</body>
</html>

```

尽管 Vue 主要是为构建 Web 应用而设计的，但它绝不仅仅局限于浏览器。你还可以：

-   配合 [Electron](https://www.electronjs.org/) 或 [Wails](https://wails.io) 构建桌面应用
-   配合 [Ionic Vue](https://ionicframework.com/docs/vue/overview) 构建移动端应用
-   使用 [Quasar](https://quasar.dev/) 或 [Tauri](https://tauri.app) 用同一套代码同时开发桌面端和移动端应用
-   使用 [TresJS](https://tresjs.org/) 构建 3D WebGL 体验
-   使用 Vue 的[自定义渲染 API](https://cn.vuejs.org/api/custom-renderer.html) 来构建自定义渲染器，比如针对[终端命令行](https://github.com/vue-terminal/vue-termui)的！