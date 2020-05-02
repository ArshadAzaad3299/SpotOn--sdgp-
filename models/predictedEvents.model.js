
const mongoose = require('mongoose')

const Schema = mongoose.Schema;

const predictedEventsSchema = new Schema({

    ID: {
        type: String,
        required: true

    },
    Title: {
        type: String,
        required: true

    }

},
);

const predictedevents = mongoose.model('predictedevents', predictedEventsSchema);

module.exports = predictedevents;