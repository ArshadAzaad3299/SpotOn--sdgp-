
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Is Trending Now
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const isittrendingnowSchema = new Schema({

    trendingNow: {
        type: String,
        required: true

    }

},
);

const isTrendingNow = mongoose.model('isittrendingnows', isittrendingnowSchema);

module.exports = isTrendingNow;