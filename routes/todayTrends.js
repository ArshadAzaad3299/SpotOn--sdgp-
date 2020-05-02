const router = require('express').Router();
let TodayTopSearches = require('../models/todayTrends.model');

const mongoose = require('mongoose');

router.route('/').get((req, res) => {
    mongoose.connect('mongodb://localhost:27017/' + 'whatIsSearchedToday' + '?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false', { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });

    const connection = mongoose.connection;

    //log if connection to Mongo Succes
    connection.once('open', () => {
        console.log("MongoDB Database connection Success to Get Today Whats trending");
    })

    TodayTopSearches.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})




module.exports = router;