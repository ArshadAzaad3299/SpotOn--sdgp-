
import { DisappearedLoading } from 'react-loadingg';
import NoInternet from '../home-component/NoInternet'
// import axios from 'axios';
import { Offline, Online } from "react-detect-offline";


import React from 'react';


class loading extends React.Component {

    render() {
        setTimeout(() => window.location = "./results", 20000);
        // setTimeout(() => axios.get('http://localhost:5000/search/add/load/'), 5000);
        return (
            <div>
                {this.ShowAlertWithDelay}
                <Offline>        
                    <NoInternet></NoInternet>
                </Offline>
                
                <Online>                
                    <DisappearedLoading size="small"></DisappearedLoading>
                </Online>



            </div>

        )

    }
}


export default loading;