import React, { Component } from 'react';
import axios from 'axios';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CategoryName from './CategoryName'




const TopSearch = props => (


    <div>
        <div class="box-newsresults">
            <Card style={{ backgroundColor: "#353431", width: "300px", color: 'white', padding: '10px' }}>
                <CardHeader
                    title={props.topresults.title}
                ></CardHeader>

                
            </Card>
            <div>

            </div>

        </div>



    </div >
)


export default class ExercisesList extends Component {

    constructor(props) {
        super(props);


        this.state = { results: [] }


    }

    componentDidMount() {
        axios.get('http://localhost:5000/search/results/categoryrelated')
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
                <br></br>
                <h1 className="topics" style={{ color: "white", textAlign: 'left' }}>Facts Related to<CategoryName></CategoryName></h1>
                {/* <h1>Hello</h1> */}
                <div>{this.resultList()}</div>

            </div>
        )
    }
}