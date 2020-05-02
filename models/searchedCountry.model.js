
const mongoose = require('mongoose')

const Schema = mongoose.Schema;

const searchedCountrySchema = new Schema({

    geoName: {
        type: String,
        required: true

    },
    name: {
        type: String,
        required: true

    }

},
);

const SearchedCountry = mongoose.model('searchedcountrys', searchedCountrySchema);

module.exports = SearchedCountry;