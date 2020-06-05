
//Importing Required Classes
import { DisappearedLoading } from 'react-loadingg';
import axios from 'axios';
import React from 'react';


// Class which loads to top searches UI

class loading extends React.Component {

/*This Component runs first once the component is rendered
This is the best place to make API calls since, at this point, the component has been mounted and is available to the DOM*/

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


//renders to UI (FrontEnd)
    render() {

        // Action to take place after 2 seconds  (go to specified location)
        setTimeout(() => window.location = "../top", 10000);
        return (
            <div>
                {this.ShowAlertWithDelay}
                <DisappearedLoading size="small"></DisappearedLoading>

            </div>
        )

    }
}


export default loading;