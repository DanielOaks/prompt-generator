const path = require('path');
const VueLoaderPlugin = require('vue-loader/lib/plugin')

module.exports = {
  entry: './_src/index.js',
  output: {
    filename: 'main.js',
    path: path.resolve(__dirname),//, 'dist'),
  },
  resolve: {
      alias: {
          vue: 'vue/dist/vue.js'
      },
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ]
      },
      {
        test: /\.scss$/,
        use: [
          'vue-style-loader',
          'css-loader',
          'sass-loader'
        ]
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: file => (
          /node_modules/.test(file) &&
          !/\.vue\.js/.test(file)
        )
      },
    ]
  },
  plugins: [
    // make sure to include the plugin!
    new VueLoaderPlugin()
  ],
};