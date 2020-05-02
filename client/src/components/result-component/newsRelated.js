import React, { Component } from 'react';
import axios from 'axios';



import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Typography from '@material-ui/core/Typography';
import Skeleton from '@material-ui/lab/Skeleton';
import Button from '@material-ui/core/Button';





const TopSearch = props => (


    <div>
        <div class="box-newsresults">
            <Card style={{ backgroundColor: "#353431", width: "300px", color: 'white', padding: '10px' }}>
                <CardHeader
                    title={props.topresults.title}
                ></CardHeader>

                <CardMedia
                    style={{ height: 0, paddingTop: '56.25%' }}
                    image={props.topresults.img}
                    title="lorem ipsum"
                />
                <CardContent>

                    <React.Fragment>
                        <Skeleton animation="wave" height={10} style={{ marginBottom: 6 }} />
                    </React.Fragment>
                    <Typography variant="body2" component="p" style={{ textAlign: 'justify' }}>
                        {props.topresults.desc}
                    </Typography>

                </CardContent>
                <Button size="small" color="primary" style={{ position: 'relative', left: '80px' }}>
                    <a href={props.topresults.link} style={{ textDecoration: 'none', color: '#A0E8F6' }}>Learn More</a>

                </Button>
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
        axios.get('http://localhost:5000/search/results/newsrelated')
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
                <h1 className="topics" style={{ color: "white", textAlign: 'left' }}>News Related</h1>
                {/* <h1>Hello</h1> */}
                <div>{this.resultList()}</div>

            </div>
        )
    }
}