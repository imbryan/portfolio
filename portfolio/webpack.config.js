const path = require('path');

module.exports = {
    entry: './assets/index.js', // Path to input file
    output: {
        filename: 'index-bundle.js', // Output bundle name
        path: path.resolve(__dirname, './static/js/bundles'), // Path to static directory
    },
    module: {
        rules: [
            {
                test: /\.(js|jxs)$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: { presets: ["@babel/preset-env", "@babel/preset-react"] }
            },
        ]
    }
}
