
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Today Trends
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const todayTrendsSchema = new Schema({

    index: {
        type: Number,
        required: true,
        trim: true,
        unique: true

    },
    query: {
        type: String,
        required: true
    },

},
);

const whatIsSearchedToday = mongoose.model('whatissearchedtodays', todayTrendsSchema);

module.exports = whatIsSearchedToday;