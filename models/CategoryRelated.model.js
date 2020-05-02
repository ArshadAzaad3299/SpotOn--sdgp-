
const mongoose = require('mongoose')

const Schema = mongoose.Schema;

const CategoryrelatedSchema = new Schema({

    title: {
        type: String,
        required: true

    }

},
);

const CategoryRelated = mongoose.model('newscategoryrelateds', CategoryrelatedSchema);

module.exports = CategoryRelated;