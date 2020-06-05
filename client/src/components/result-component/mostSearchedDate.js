import React, { Component } from 'react';
import axios from 'axios';
import Didyouknow from '../../img/didyouknow.png';
import Fab from '@material-ui/core/Fab';

import TextField from '@material-ui/core/TextField';
import Card from '@material-ui/core/Card';



//constant to populate results from array and mongo column id
const TopSearch = props => (
    <div>

        <TextField
            inputProps={{ style: { color: '#A29898', textAlign: 'center' } }}
            disabled
            textAlign="center"
            error
            id="standard-error-helper-text"
            defaultValue={props.topresults.MostSearchedDate}
        />
    </div >
)
//This class displays the most searched date of the keyword searched
export default class MostSearchedDateClass extends Component {
    constructor(props) {
        super(props);


        this.state = { results: [] }


    }
/*This Component runs first once the component is rendered
This is the best place to make API calls since, at this point, the component has been mounted and is available to the DOM*/

    componentDidMount() {
        axios.get('http://localhost:5000/search/results/mostsearcheddate')
            .then(response => {
                this.setState({ results: response.data })
                // console.log(se.username)
            })
            .catch((error) => {
                console.log(error)
            })
    }

//this functions maps the array values
    resultList() {
        return this.state.results.map(currentSearch => {
            return <TopSearch topresults={currentSearch} key={currentSearch._id} />
        })
    }

//
    render() {
        return (
            <div>
                <Card style={{ backgroundColor: '#3A3E46', padding: '30px', width: '320px' , borderRadius:'10px'}}>
                    <img src={Didyouknow} alt="searchedcountryGraph" width="300px" height="150px"></img>
                    <Fab variant="extended"
                    style={{backgroundColor:'#633d52', color: 'white'}}>
                        This term was Trending On
                    </Fab>
                    <br></br>
                    <br></br>
                    <div>{this.resultList()}</div>
                </Card>

            </div>
        )
    }
}