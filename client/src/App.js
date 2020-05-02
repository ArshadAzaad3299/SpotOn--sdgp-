import React from 'react';
import './App.css';
// import "bootstrap/dist/css/bootstrap.min.css";


import {BrowserRouter as Router,Route} from "react-router-dom";   
import FirstPage from './components/home-component/search-bar'
import Loading from './components/home-component/Loading'
import Welcome from './components/welcome'
import topSearchesUi from './components/top-searches/topSearches-UI'
import NavBar from './components/NavBar'
import resultsPage from './components/result-component/results'
import Browse from './components/browse-component/browse'
import BrowseLoading from './components/browse-component/BrowseLoading'
import BrowseResults from './components/browse-component/Browse-results'


import isTrendinggauge from './components/result-component/isTrendingGauge'
import summary from './components/result-component/summary'
import YouTubeResults from './components/result-component/youtubeResults'
import RisingSearches from './components/result-component/risingSearches'
import Newsrelated from './components/result-component/newsRelated'
import SearchedCountry from './components/result-component/SearchedCountry'
import MostSearchedDate from './components/result-component/mostSearchedDate'
import PredictedEvents from './components/result-component/predictedevents'
import CategoryRelated from './components/result-component/CategoryRelated'
import NoInternet from './components/home-component/NoInternet'
import Subscribe from './components/subscribe/subscribe'



import LoadtoTop from './components/top-searches/loadto-topSearches'

function App() {
  return (
    <div className="App">

      <Router>
        <NavBar></NavBar>
      
      

      <Route path="/" exact component={Welcome}/>
      <Route path="/spoton" exact component={FirstPage}/>
      <Route path="/spoton/search" exact component={FirstPage}/>
      <Route path="/spoton/search/loading" exact component={Loading}/>
      <Route path="/spoton/top" exact component={topSearchesUi}/>
      <Route path="/spoton/search/results" exact component={resultsPage}/>
      <Route path="/spoton/browse" exact component={Browse}/>
      <Route path="/spoton/top/load" exact component={LoadtoTop}/>
      <Route path="/spoton/top/subscribe" exact component={Subscribe}/>




      <Route path="/spoton/search/results/summary" exact component={summary}/>
      <Route path="/spoton/search/results/isTrending" exact component={isTrendinggauge}/>
      <Route path="/spoton/search/results/youtubeResults" exact component={YouTubeResults}/>
      <Route path="/spoton/search/results/risingSearches" exact component={RisingSearches}/>
      <Route path="/spoton/search/results/newsrelated" exact component={Newsrelated}/>
      <Route path="/spoton/search/results/searchedcountry" exact component={SearchedCountry}/>
      <Route path="/spoton/search/results/mostsearcheddate" exact component={MostSearchedDate}/>
      <Route path="/spoton/search/results/predictedevents" exact component={PredictedEvents}/>
      <Route path="/spoton/search/results/categoryrelated" exact component={CategoryRelated}/>
      <Route path="/spoton/search/nointernet" exact component={NoInternet}/>
      <Route path="/spoton/browse/loading" exact component={BrowseLoading}/>
      <Route path="/spoton/browse/results" exact component={BrowseResults}/>


      


      {/* <Route path="/browse" exact component={Sample}/> */}
      {/* <Route path="/home" exact component={Sample}/> */}

      </Router>
      

      </div>
    
  );
}

export default App;
