
import { DisappearedLoading } from 'react-loadingg';
import axios from 'axios';


import React from 'react';


class loading extends React.Component {
    componentDidMount() {
        axios.get('http://localhost:5000/todayTrends/')
            .then(response => {
                this.setState({ results: response.data })
                // console.log(se.username)
            })
            .catch((error) => {
                console.log(error)
            })
    }



    render() {
        setTimeout(() => window.location = "../top", 2000);
        return (
            <div>
                {this.ShowAlertWithDelay}
                <DisappearedLoading size="small"></DisappearedLoading>

            </div>

        )

    }
}


export default loading;