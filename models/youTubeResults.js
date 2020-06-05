
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Youtube Results
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const youtubeSchema = new Schema({

    title: {
        type: String,
        required: true

    },
    link: {
        type: String,
        required: true

    }

},
);

const YouTubeResults = mongoose.model('youtuberesults', youtubeSchema);

module.exports = YouTubeResults;