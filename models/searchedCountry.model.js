
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Searched Country
//The Schema is passed to the router when required to collect values from MongoDB Collection
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