
const mongoose = require('mongoose')

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