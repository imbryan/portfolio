const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const isProduction = process.env.NODE_ENV === 'production';

module.exports = {
    entry: './assets/index.js', // Path to input file
    output: {
        filename: 'index-bundle.js', // Output bundle name
        path: path.resolve(__dirname, './static/js/bundles'), // Path to static directory
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                options: { presets: ["@babel/preset-env", "@babel/preset-react"] }
            },
            {
                test: /\.scss$/,
                use: [
                    isProduction ? MiniCssExtractPlugin.loader : 'style-loader',
                    'css-loader',
                    'sass-loader',
                ],
            },
        ]
    },
    plugins: [
        ...(isProduction ? [new MiniCssExtractPlugin({
            filename: 'styles.css',
        })] : []),
    ],
    mode: isProduction ? 'production' : 'development',
}
