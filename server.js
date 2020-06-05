const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const path = require('path');

require('dotenv').config();

const app = express();

//Connect To Port
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());


// routers for appp
const searchRouter = require('./routes/searchKeyword');
const resultsRouter = require('./routes/dashboard.results.route');
const browseRouter = require('./routes/browse');

const subscribeRouter = require('./routes/subscribe');
const todayTrendsRouter = require('./routes/todayTrends');

app.use('/search', searchRouter);
app.use('/search/results', resultsRouter);
app.use('/browse', browseRouter);
app.use('/subscribe', subscribeRouter);
app.use('/todayTrends', todayTrendsRouter)




//Build Process Fro Heruko
if(process.env.NODE_ENV === 'production'){
    app.use(express.static('client/build'));
    app.get('*',(req,res)=>{
        res.sendFile(path.resolve(__dirname,'client','build','index.html'));
    })
}

//log if port connection success
app.listen(port, () => {    
    console.log('Server is running on port : ' + port);
})
