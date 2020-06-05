//impoorting Modules
import React, { Component } from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';


//constant which populates the array based on the MongoDb Collection scheme
const TopSearch = props => (
    <div>
        <div className="risingSearches">
            <Button variant="outlined" color="primary" style={{ color: 'white' ,fontSize:'11px'}} >
                {props.topresults.tweet}
            </Button>
        </div>

    </div >
)

//This class displays top 5 tweets from Mongo DB
export default class TopFiveTweets extends Component {
    constructor(props) {
        super(props);


        this.state = { results: [] }


    }
    /*This Component runs first once the component is rendered
This is the best place to make API calls since, at this point, the component has been mounted and is available to the DOM*/

    componentDidMount() {
        axios.get('http://localhost:5000/search/results/topfivetweets')
            .then(response => {
                this.setState({ results: response.data })
                // console.log(se.username)
            })
            .catch((error) => {
                console.log(error)
            })
    }

//Map the array accoring to its values from MongoDb
    resultList() {
        return this.state.results.map(currentSearch => {
            return <TopSearch topresults={currentSearch} key={currentSearch._id} />
        })
    }

//Render displays componenents to the UI
    render() {
        return (
            <div>
                <div className="DboxFull">
                    <Paper elevation={0} style={{ backgroundColor: '#3A3E46', width: '450px' }} >
                        <div className="dBox">
                            <p className="topics" style ={{ 
                                color: "#FCB415", 
                                textAlign: 'left', 
                                fontFamily: 'Arial', 
                                fontSize: '30px', 
                                borderBottom:'1px Solid #FCB415 ',
                                paddingBottom: '6px'
                                
                                }}>Top 5 Tweets</p>

                            <div>{this.resultList()}</div>
                        </div>

                    </Paper>
                </div>
                <br></br>
            </div>
        )
    }
}