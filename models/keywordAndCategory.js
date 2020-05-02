
const mongoose = require('mongoose')

const Schema = mongoose.Schema;

const nameSchema = new Schema({

    keyword: {
        type: String,
        required: true

    },
    Category: {
        type: String,
        required: true

    }

},
);

const NameAndCategory = mongoose.model('keywordandcategorys', nameSchema);

module.exports = NameAndCategory;