import React, { Component } from 'react';
import axios from 'axios';
import Gauge from 'react-svg-gauge';


const TopSearch = props => (


    <div className="topTrendingRow">
        <div >
            <div >
                <Gauge width={400} height={320} label="Trending Now ?" color='#FFDA83' value={props.topresults.trendingNow}
                    valueLabelStyle={{
                        fontSize: 60,
                        fontFamily: 'Arial',
                        fill: 'white'
                    }}
                />
            </div>
        </div>
        <br></br>
    </div>
)

export default class ExercisesList extends Component {
    constructor(props) {
        super(props)

        this.state = { results: [] }
    }
    /*This Component runs first once the component is rendered
This is the best place to make API calls since, at this point, the component has been mounted and is available to the DOM*/

    componentDidMount() {
        axios.get('http://localhost:5000/search/results/isTrending/')
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