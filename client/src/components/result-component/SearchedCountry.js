// import GraphSearchCountry from '../searchedcountry.png'
import Graph1 from './searchedcountry.png';
import React from 'react';




class SearchCountry extends React.Component {



    // componentDidMount() {
    //     axios.get('http://localhost:5000/search/results/newsrelated')
    //         .then(response => {
    //             this.setState({ results: response.data })
    //             // console.log(se.username)
    //         })
    //         .catch((error) => {
    //             console.log(error)
    //         })
    // }



    render() {

        return (
            <div>
                <img src={Graph1} alt="logo" />
            </div>

        )

    }
}


export default SearchCountry;