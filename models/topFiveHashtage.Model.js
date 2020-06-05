
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Top Hashtags
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const Top5Tweets = new Schema({

    tweet: {
        type: String,
        required: true

    }

},
);

const TopFiveTweetsSchema = mongoose.model('topfivehashtags', Top5Tweets);

module.exports = TopFiveTweetsSchema;