
import { CountdownCircleTimer } from 'react-countdown-circle-timer'
import React from 'react';


class NoInternet extends React.Component {



    render() {
        setTimeout(() => window.location = "/", 3000);
        return (
            <div>
                <div className="nointernet">
                    {/* <img src={Disconnected} alt="searchedcountryGraph" width="200px" height="150px"></img> */}
                    <h2 style={{ color: 'white' }}>Looks like You Are Not Connected</h2>
                    <h2 style={{ color: 'white' }}>Reconnecting</h2>

                    <CountdownCircleTimer
                        isPlaying
                        duration={3}
                        size='100'
                        strokeWidth='2'
                        colors={[['#004777', 0.33], ['#F7B801', 0.33], ['#A30000']]}
                    >
                        {({ remainingTime }) => remainingTime}
                    </CountdownCircleTimer>
                </div>
            </div>

        )

    }
}


export default NoInternet;