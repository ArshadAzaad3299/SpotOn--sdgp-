
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Similar Searches
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const similarSearchesSchema = new Schema({

    query: {
        type: String,
        required: true

    }

},
);

const SimilarSearches = mongoose.model('topsearches', similarSearchesSchema);

module.exports = SimilarSearches;