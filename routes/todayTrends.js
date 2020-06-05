//this router class lets user to view top treniding topics today 

const router = require('express').Router();
let TodayTopSearches = require('../models/todayTrends.model');

const mongoose = require('mongoose');

//route for top trends (/)
router.route('/').get((req, res) => {
    whatsTrendingTodayPython();

    //local db 
    // mongoose.connect('mongodb://localhost:27017/' + 'whatIsSearchedToday' + '?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false', { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });
    
    //mongodb Atlas
    mongoose.connect('mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/whatIsSearchedToday?authSource=admin&replicaSet=sdgp1-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true', { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });


    const connection = mongoose.connection;

    //log if connection to Mongo Succes
    connection.once('open', () => {
        console.log("MongoDB Database connection Success to Get Today Whats trending");
    })
    //using mongooose scheme find the collection and required values
    TodayTopSearches.find()
        .then(users => res.json(users))
        .catch(err => res.status(400).json('Error:' + err));
})


//function to run python file what is Searched Today 
function whatsTrendingTodayPython(req, res) {

    var spawn = require("child_process").spawn;
    var process = spawn('python', ["./pyFiles/whatisSearchedToday.py"
    ]);
//log running python file
    console.log("Running PyThon Script [Whats Trending Now]")
}

module.exports = router;