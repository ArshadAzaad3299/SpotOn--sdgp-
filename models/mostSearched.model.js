
const mongoose = require('mongoose')

const Schema = mongoose.Schema;

const mostSearchedDateSchema = new Schema({

    MostSearchedDate: {
        type: String,
        required: true

    },


},
);

const mostSearchedDate = mongoose.model('mostsearcheddates', mostSearchedDateSchema);

module.exports = mostSearchedDate;