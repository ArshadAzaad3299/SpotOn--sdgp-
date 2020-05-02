/*This class lets front and backend interact using module Axios */

const mongoose = require('mongoose');
const router = require('express').Router();
var keyword;
var category;
var dbName;


router.route('/add').post((req, res) => {
    const searchTerm = req.body.search;
    res.json(searchTerm);
    keyword = searchTerm;
    console.log('Searched Keyword : ' + keyword);
    setDatabaseName();
    runPythonScript();
    
});


router.route('/add/load').get((req, res) => {
    connectDatabase()
    console.log('Datbase connected after 5 sec')
    var spawn = require("child_process").spawn;
    var process = spawn('python', ["./pyFiles/Graph.py",keyword]);
    console.log('Processing Graphs');
})


function  setDatabaseName() {
    var spawn = require('child_process').spawn,
    ls = spawn('python', ['./pyFiles/setDatabaseName.py', keyword]);

    ls.stdout.on('data', function (data) {
        console.log('stdout: ' + data);
        dbName = String(data);
        console.log("DataBase Name : " + dbName)
    });
    
    ls.stderr.on('data', function (data) {
        console.log('stderr: ' + data);
    });

}
function connectDatabase() {
    
    // mongoose.connect('mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/' + dbName + '?retryWrites=true&w=majority', { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });

    mongoose.connect('mongodb://localhost:27017/' + dbName + '?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false', { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });

    const connection = mongoose.connection;

    //log if connection to Mongo Succes
    connection.once('open', () => {
        console.log("MongoDB Database connection Success to " + dbName);
    })
    
}

function runPythonScript(req, res) {

    category = 'health_environment';
    console.log('Predicted Category : ' + category);

    console.log('Searched Keyword Passed To Python File');


    var spawn = require("child_process").spawn;
    var process = spawn('python', ["./pyFiles/predictedData.py",keyword, category]);

    console.log("RUNNING PYTHON SCRIPT")
}

module.exports = router, runPythonScript;
