
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Top Tweets
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const Top5Tweets = new Schema({

    Text: {
        type: String,
        required: true

    }

},
);

const TopFiveTweetsSchema = mongoose.model('topfivetweets', Top5Tweets);

module.exports = TopFiveTweetsSchema;