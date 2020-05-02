
const mongoose = require('mongoose')

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