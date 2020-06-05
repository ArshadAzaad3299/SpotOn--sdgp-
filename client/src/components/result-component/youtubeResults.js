import React, { Component } from 'react';
import axios from 'axios';

import YouTube from 'react-youtube';


const opts = {
    height: '190',
    width: '340',

};

const TopSearch = props => (


    <div>

        <div >
            <div class="box-youtube">
                <div>
                    <YouTube videoId={props.topresults.link.replace('watch?v=', '/')}
                        opts={opts}
                    />
                    <p style={{ color: 'white', textAlign: 'center', maxWidth: '300px' }}>     {props.topresults.title}</p>
                </div>
            </div>
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
        axios.get('http://localhost:5000/search/results/youtube')
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
            
            <div >
                <h1 className="topics" style={{ color: "white", textAlign: 'left' }}>YouTube Related</h1>
                <div>{this.resultList()}</div>
            </div>
        )
    }
}