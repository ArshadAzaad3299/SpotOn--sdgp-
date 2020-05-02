import React from 'react';


import Summary from './summary'
import IsTrendingGauge from './isTrendingGauge'
import KeywordAndCategory from './keywordAndCategory'
import YouTubeResults from './youtubeResults'
import RisingSearches from './risingSearches'
import NewsResults from './newsRelated'
import Graph1 from './searchedcountry.png';
import Graph2 from './searcheddates.png';
import MostSearchedDate from './mostSearchedDate'
import SimilarSearches from './similarsearches'
import PredictedEvent from './predictedevents'
import CategoryRelated from './CategoryRelated'





class loading extends React.Component {


    render() {
        return (
            <div>

                <div className="line-1">
                    <KeywordAndCategory></KeywordAndCategory>
                </div>
                <div className="line-2">
                    <div className="line-2-left">
                        <Summary></Summary>
                    </div>
                    <div className="line-2-right">
                        <SimilarSearches></SimilarSearches>

                    </div>
                    <div className="line-2-right">
                        <img src={Graph1} alt="searchedcountryGraph" width="650px" height="350px" className="graph-top"></img>
                    </div>


                </div>

                <div className="graph-line-1">
                    <div className="graph1">
                        <RisingSearches></RisingSearches>

                    </div>
                    <div className="graph2">
                        <img src={Graph2} alt="searchedcountryGraph" width="1100px" height="400px"></img>
                    </div>

                </div>

                <div className="line-3">
                    <div className="line3-1">
                        <IsTrendingGauge></IsTrendingGauge>


                    </div>
                </div>

                <div className="line-4">
                    <div className="line-4-left">
                        <MostSearchedDate></MostSearchedDate>
                    </div>
                    <div className="line-4-right">
                        <RisingSearches></RisingSearches>


                    </div>
                    <div className="line-4-right">
                        <PredictedEvent></PredictedEvent>

                    </div>


                </div>


                <div className="line-5">
                    <CategoryRelated></CategoryRelated>
                </div>
                <br></br>
                <div className='line-6'>
                    <YouTubeResults></YouTubeResults>
                </div>
                <div className='line-7'>
                    <NewsResults></NewsResults>
                </div>


            </div>

        )

    }
}


export default loading;