const path = require('path');

module.exports = {
    entry: './assets/index.js', // Path to input file
    output: {
        filename: 'index-bundle.js', // Output bundle name
        path: path.resolve(__dirname, './static/js/bundles'), // Path to static directory
    },
}