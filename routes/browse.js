const mongoose = require('mongoose');
const router = require('express').Router();
var keyword;
var userPreferences;
let BrowseResults = require('../models/browseresults.model');

/*This route class interacts with the browse component in react which handles the post and get requests 
through axios
Then the python scripts are called within functions (News Prediction) and values are stored in MongoDB*/

router.route('/input').post((req, res) => {
    const searchTerm = req.body.search;
    res.json(searchTerm);
    keyword = searchTerm;
    console.log('User Preferences : ' + keyword);
    runPythonScript();
});

router.route('/browseresults').get((req, res) => {

    console.log('Browse Results')
    BrowseResults.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})

router.route('/browse').get((req, res) => {
    runPythonScript2();
})


function runPythonScript(req, res) {
    var spawn = require('child_process').spawn,
        ls = spawn('python', ['./pyFiles/getBrowseResults.py', keyword]);

    mongoose.connect('mongodb://localhost:27017/' + 'browse' + '?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false', { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });

    const connection = mongoose.connection;

    //log if connection to Mongo Succes
    connection.once('open', () => {
        console.log("MongoDB Database connection Success to Browse DB ");
    })

}


function runPythonScript2(req, res) {
    var spawn = require('child_process').spawn,
        ls = spawn('python', ['./pyFiles/newsPrediction.py']);

    console.log("Categorizing latest news to topics");
}

module.exports = router;
