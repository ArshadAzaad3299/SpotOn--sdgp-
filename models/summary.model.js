
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection Summary
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const summarySchema = new Schema({

    summary: {
        type: String,
        required: true

    }

},
);

const Summary = mongoose.model('summarys', summarySchema);

module.exports = Summary;