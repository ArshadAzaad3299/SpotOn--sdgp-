import React, { Component } from 'react';
import axios from 'axios';
import Button from '@material-ui/core/Button';
import Paper from '@material-ui/core/Paper';


//constant which populates the array based on the MongoDb Collection Scheme passed From Node
const TopSearch = props => (
    <div>
        <div className="risingSearches">
            {props.topresults.ID}
            <br></br>
            <Button variant="outlined" color="primary" style={{ color: 'white', paddingBottom:'5px' }} >
                <a href={props.topresults.Title} style={{ textDecoration: 'none', color: '#A0E8F6' }}>Learn More</a>
            </Button>
        </div>

    </div >
)

//This class Displays the Predcited events For User Searched Keyword

export default class PredictedEvents extends Component {
    constructor(props) {
        super(props);


        this.state = { results: [] }


    }
    /*This Component runs first once the component is rendered
This is the best place to make API calls since, at this point, the component has been mounted and is available to the DOM*/

    componentDidMount() {
        axios.get('http://localhost:5000/search/results/predictedevents')
            .then(response => {
                this.setState({ results: response.data })
                // console.log(se.username)
            })
            .catch((error) => {
                console.log(error)
            })
    }

//mapping the values of the array
    resultList() {
        return this.state.results.map(currentSearch => {
            return <TopSearch topresults={currentSearch} key={currentSearch._id} />
        })
    }

    render() {
        return (
            <div>
                <div className="DboxFull">
                    <Paper elevation={0} style={{ backgroundColor: '#3A3E46', width: '450px' }} >
                        <div className="dBox">
                            <p className="topics" style={{
                                color: "#FCB415",
                                textAlign: 'left',
                                fontFamily: 'Arial',
                                fontSize: '30px',
                                borderBottom: '1px Solid #FCB415 ',
                                paddingBottom: '6px'

                            }}>Why Trending ?</p>

                            <div>{this.resultList()}</div>
                        </div>

                    </Paper>
                </div>
                <br></br>
            </div>
        )
    }
}