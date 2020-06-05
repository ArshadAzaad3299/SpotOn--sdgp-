
//Using Module Mongoose
const mongoose = require('mongoose')

//This Schema is the structure of the MongoDB Collection News Search
//The Schema is passed to the router when required to collect values from MongoDB Collection
const Schema = mongoose.Schema;

const newsRelatedSchema = new Schema({

    title: {
        type: String,
        required: true

    },
    desc: {
        type: String,
        required: true

    },
    link: {
        type: String,
        required: true

    },
    img: {
        type: String,
        required: true

    },


},
);

const NewsRelated = mongoose.model('newssearchs', newsRelatedSchema);

module.exports = NewsRelated;