import React, { Component } from 'react';
import axios from 'axios';



const TopSearch = props => (
    <div>

        {props.topresults.Category}

    </div >
)

export default class ExercisesList extends Component {
    constructor(props) {
        super(props);


        this.state = { results: [] }


    }

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