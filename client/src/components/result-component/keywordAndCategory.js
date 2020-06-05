import React, { Component } from 'react';
import axios from 'axios';

import TextField from '@material-ui/core/TextField';


const TopSearch = props => (
    <div>

        <br></br>
        <br></br>
        <TextField
            required
            type="search"
            // id="standard-basic"
            className="textfield"
            inputProps={{ style: { color: '#A29898', width: 400, backgroundColor: '#4E4B4B', WebkitBorderRadius: '15px', height: 35, textAlign: "center", fontSize: "23px" } }}
            value={props.topresults.keyword}
            placeholder="Search"
            disabled

        />
        <br></br>
        <br></br>
        <br></br>
        <div>
            <h2 style={{ color: 'white', borderBottom: '2px Solid #FF6565', display: 'inline', paddingBottom: '6px' }}>        {props.topresults.Category}
            </h2>

        </div>





    </div >
)

export default class ExercisesList extends Component {
    constructor(props) {
        super(props);


        this.state = { results: [] }


    }
    /*This Component runs first once the component is rendered
This is the best place to make API calls since, at this point, the component has been mounted and is available to the DOM*/

    componentDidMount() {
        axios.get('http://localhost:5000/search/results/nameAndCategory')
            .then(response => {
                this.setState({ results: response.data })
                // console.log(se.username)
            })
            .catch((error) => {
                console.log(error)
            })
    }


    resultList() {
        return this.state.results.map(currentSearch => {
            return <TopSearch topresults={currentSearch} key={currentSearch._id} />
        })
    }


    render() {
        return (
            <div>

                <div>{this.resultList()}</div>

            </div>
        )
    }
}