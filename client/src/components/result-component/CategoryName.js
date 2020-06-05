import React, { Component } from 'react';
import axios from 'axios';


//constatant to populate results from Array
const TopSearch = props => (
    <div>

        {props.topresults.Category}

    </div >
)

//Class which populates the Category Name

export default class CategoryName extends Component {
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