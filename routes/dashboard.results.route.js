const router = require('express').Router();
let Summary = require('../models/summary.model');
let isTrending = require ('../models/istrending.mode');
let nameAndCategory = require('../models/keywordAndCategory');
let youTubeResults = require('../models/youTubeResults');
let risingSearches = require('../models/risingSearches.model');
let newsRelated = require('../models/newsSearch.model');
let searchedCountry = require('../models/searchedCountry.model');
let MostSearched = require('../models/mostSearched.model');
let Similarsearches = require('../models/similarSearches.mode');
let PredictedEvents = require('../models/predictedEvents.model');
let CategoryRelated = require('../models/CategoryRelated.model');





const mongoose = require('mongoose');

router.route('/summary/').get((req, res) => {
    console.log('summary requested')

    Summary.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})


router.route('/isTrending/').get((req, res) => {
    console.log('is Trending requested')
    isTrending.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/nameAndCategory/').get((req, res) => {
    console.log('Name and Category requested')

    nameAndCategory.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/youtube/').get((req, res) => {
    console.log('Youtube Results requested')

    youTubeResults.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/risingSearches/').get((req, res) => {
    console.log('RisingSearches Results requested')

    risingSearches.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/newsrelated/').get((req, res) => {
    console.log('News Related requested')

    newsRelated.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/searchedcountry/').get((req, res) => {
    console.log('Searched Country Results requested')

    searchedCountry.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/mostsearcheddate/').get((req, res) => {
    console.log('Most Searched Date requested')

    MostSearched.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/similarsearches/').get((req, res) => {
    console.log('Similar Searches requested')

    Similarsearches.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/predictedevents/').get((req, res) => {
    console.log('Predicted Events requested')

    PredictedEvents.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/categoryrelated/').get((req, res) => {
    console.log('category related requested')

    CategoryRelated.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));

        
})






module.exports = router;