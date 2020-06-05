
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Most Searched Dates
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const mostSearchedDateSchema = new Schema({

    MostSearchedDate: {
        type: String,
        required: true

    },


},
);

const mostSearchedDate = mongoose.model('mostsearcheddates', mostSearchedDateSchema);

module.exports = mostSearchedDate;