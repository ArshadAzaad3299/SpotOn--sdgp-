
const mongoose = require('mongoose')

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