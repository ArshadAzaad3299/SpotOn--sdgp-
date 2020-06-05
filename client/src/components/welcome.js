
import { LoopCircleLoading } from 'react-loadingg';
import Logo from '../SpotOn Logo.png'
import { Offline, Online } from "react-detect-offline";
import NoInternet from './home-component/NoInternet'

import React from 'react';

//This class Contains the Welcome Page displaying the App Logo and then following to the home page
class Welcome extends React.Component {

//render which retuns a reference to the component
    render() {
        setTimeout(() => window.location = "./spoton", 4000);

        return (
            <div>
                <img src={Logo} width='200px' height="200px" className="AppLogo" alt="Spot On"></img>

                <Online>
                    <LoopCircleLoading size="small" className="welcomeAnimation" ></LoopCircleLoading>
                </Online>

                <Offline>
                    <NoInternet></NoInternet>
                </Offline>
            </div>

        )

    }
}


export default Welcome;