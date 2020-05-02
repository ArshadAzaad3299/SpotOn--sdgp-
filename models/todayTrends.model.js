
const mongoose = require('mongoose')

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