
const mongoose = require('mongoose')

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