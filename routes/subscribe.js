/*router class that gets a keyword from react and passes to python file which
sends top trends to user emial*/

const router = require('express').Router();
var keyword;

const mongoose = require('mongoose');


//router route of subscribe component1w1
router.route('/subscribe').post((req, res) => {
    const searchTerm = req.body.search;
    res.json(searchTerm);
    keyword = searchTerm;
    console.log("subscribe " + keyword)
    runPython()
});

//function to run python script which sends top trends to user email

function runPython(){
    var spawn = require("child_process").spawn;
    var process = spawn('python', ["./pyFiles/subscribe.py", keyword]);
    console.log('Processing subscribe Python');
}


module.exports = router;