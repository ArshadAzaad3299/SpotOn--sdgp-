
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection newsData
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const BrowseResultsSchema = new Schema({

    Text: {
        type: String,
        required: true

    }
},
);

const BrowseResults = mongoose.model('newsData', BrowseResultsSchema);

module.exports = BrowseResults;