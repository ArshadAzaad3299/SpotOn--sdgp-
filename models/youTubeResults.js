
const mongoose = require('mongoose')

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