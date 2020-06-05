
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Keyword And Category
//The Schema is passed to the router when required to collect values from MongoDB Collection
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