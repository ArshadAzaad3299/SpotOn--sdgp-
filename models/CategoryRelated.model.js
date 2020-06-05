
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection News Category Related
//The Schema is passed to the router when required to collect values from MongoDB Collection
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