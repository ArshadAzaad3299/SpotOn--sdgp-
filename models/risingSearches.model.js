
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Rising Searches
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const risingSearchesSchema = new Schema({

    query: {
        type: String,
        required: true

    }

},
);

const RisingSearches = mongoose.model('risingsearches', risingSearchesSchema);

module.exports = RisingSearches;