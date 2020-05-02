
const mongoose = require('mongoose')

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