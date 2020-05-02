import React from 'react';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';
import SearchRoundedIcon from '@material-ui/icons/SearchRounded';
import Fab from '@material-ui/core/Fab';
import Alert from '@material-ui/lab/Alert';
import { Offline, Online} from "react-detect-offline";

import NoInternet from '../home-component/NoInternet'




class HomePage extends React.Component {
  constructor(props) {
    super(props);

    this.onChangeSearch = this.onChangeSearch.bind(this);
    this.onSubmit = this.onSubmit.bind(this);

    this.state = {
      search: '',

      searchError: '',


    }
  }

  validate = () => {
    let searchError: '',
      input = "Invalid input"

    if (!(this.state.search.length > 3)) {
      searchError = <div className="searchAlert"><Alert
        severity="error"
        style={{
          backgroundColor: 'transparent',
          color: '#ff1100',
          fontFamily: 'Calibri',
          maxWidth: '200px'
        }}>
        {input}
      </Alert></div>;
    }

    if (searchError) {
      this.setState({ searchError });
      return false;
    }
    return true;
  }

  onChangeSearch(e) {
    this.setState({
      search: e.target.value
    });
  }

  onSubmit(e) {
    e.preventDefault();

    const isValid = this.validate();
    if (isValid) {
      // console.log(this.state);


      const searchKeyword = {
        search: this.state.search,

      }
      axios.post('http://localhost:5000/search/add', searchKeyword)
        .then(res => console.log(res.data));

      console.log(searchKeyword);


      window.location = '/spoton/search/loading';


      this.setState({
        search: '',
        searchError: ''
      })



    }
    else {
      console.log('wrong');
    }
  }


  render() {
    return (

      <React.Fragment>
        <Online>
        <br></br><br></br>
        <br></br><br></br>
        <br></br><br></br>
        <br></br><br></br>
        <br></br>
        <br></br>
        <form>
          <TextField
            required
            type="search"
            // id="standard-basic"
            className="textfield"
            inputProps={{ style: { color: '#A29898', width: 400, backgroundColor: '#4E4B4B', WebkitBorderRadius: 24, height: 35, textAlign: "center", fontSize: "23px" } }}
            value={this.state.search}
            onChange={this.onChangeSearch}
            placeholder="Search"

          />
          <Fab className="searchBUtton" color="primary" aria-label="add" onClick={e => this.onSubmit(e)} style={{width:'65px',height:'65px'}}>

            <SearchRoundedIcon></SearchRoundedIcon>
          </Fab>

          <div style={{ color: '#eb1473' }}>{this.state.searchError}</div>

        </form>
        </Online>
        <Offline>
          <NoInternet></NoInternet>
        </Offline>
      </React.Fragment>
    );
  }
}

export default HomePage