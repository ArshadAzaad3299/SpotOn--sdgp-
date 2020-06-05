
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Predicted Events
//The Schema is passed to the router when required to collect values from MongoDB Collection
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