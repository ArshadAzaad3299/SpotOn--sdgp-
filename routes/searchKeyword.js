/*This class lets front and backend interact using module Axios */

const mongoose = require('mongoose');
const router = require('express').Router();
var keyword;
var category;
var dbName;


/* Each router specifies the url request from React and Post Method takes in values and Get Method
sends values */


/*This Function takes in the search keyword from react and assigns to variable keyword and Two other functions are called
within this method*/
router.route('/add').post((req, res) => {
    const searchTerm = req.body.search;
    res.json(searchTerm);
    keyword = searchTerm;
    console.log('Searched Keyword : ' + keyword);
    TextClassification();
    setDatabaseName();
});

/*This Function Calls The main Python Script which turns Categorises and predicts dat*/

function  TextClassification() {
    console.log("Running Text Classification")
    var spawn = require('child_process').spawn,
    ls = spawn('python', ['./pyFiles/TextClassificationPhase_01/main.py', keyword]);

    ls.stdout.on('data', function (data) {
        console.log('stdout: ' + data);
        category = String(data);
        console.log("Predicted Category : " + category)
    });
    //print on console python script output
    ls.stderr.on('data', function (data) {
        console.log('stderr: ' + data);
    });

}

//Route which connects to databse after 5 seconds callback function from React

router.route('/add/load').get((req, res) => {
    connectDatabase()
    console.log('Datbase connected after 5 sec')
    var spawn = require("child_process").spawn;
    var process = spawn('python', ["./pyFiles/Graph.py",keyword]);
    console.log('Processing Graphs');
})

router.route('/add/load1').get((req, res) => {
    connectDatabase()
    console.log('Datbase connected after 5 sec')
 
})

/*Function to set database name*/
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

/*Function to connect Database*/

function connectDatabase() {
    
    mongoose.connect('mongodb+srv://root1:sdgp1234@sdgp1-fmfys.mongodb.net/' + dbName + '?retryWrites=true&w=majority', { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });

    // mongoose.connect('mongodb://localhost:27017/' + dbName + '?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false', { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true });

    const connection = mongoose.connection;
    //log if connection to Mongo Succes
    connection.once('open', () => {
        console.log("MongoDB Database connection Success to " + dbName);
    })
    
}

// function runPythonScript(req, res) {
//     console.log(category)

//     category="health"
//     console.log('Predicted Category : ' + category);
//     console.log('Searched Keyword Passed To Python File');
//     var spawn = require("child_process").spawn;
//     var process = spawn('python', ["./pyFiles/predictedData.py",keyword, category]);

//     console.log("RUNNING PYTHON SCRIPT")
// }

module.exports = router;
