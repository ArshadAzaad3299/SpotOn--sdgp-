
const mongoose = require('mongoose')

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