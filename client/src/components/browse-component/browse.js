import React from 'react';
import axios from 'axios';
import BusinessImg from '../../img/business.jpg'
import SpaceImg from '../../img/space.jpg'
import EnterTainmentImg from '../../img/Entertainment.jpg'
import HealthImg from '../../img/Health.jpg'
import SportstImg from '../../img/sports.jpg'
import PoliticsImg from '../../img/pol.jpg'
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Radio from '@material-ui/core/Radio';

import Button from '@material-ui/core/Button';

/*
Class to Display 6 items [images] of user preferences based on Topics and allows users to pick any topic through 
a radio button and loads to page which dislpays latest topic content
*/

class BankForm extends React.Component {

    //constructor
    constructor() {
        super();
        this.onSubmit = this.onSubmit.bind(this);
        //set state of variables
        this.state = {
            price: [

            ],
            search: '',

            searchError: '',
        };
    }

    //on change search function
    onChangeSearch(e) {
        this.setState({
            search: e.target.value
        });
    }

    //on Submit Function which sends the user prefernces to node Js

    onSubmit(e) {
        e.preventDefault();
        console.log(this.state.price);

        const searchKeyword = {
            search: this.state.price,

        }
        axios.post('http://localhost:5000/browse/input', searchKeyword)
            .then(res => console.log(res.data));

        console.log(searchKeyword);

        window.location = '/spoton/browse/loading';

    }

    onPriceChange(index, e) {

        var prices = this.state.price.slice();

        prices[index] = e.target.value;

        this.setState({
            price: prices
        });
    }

    //This function runs first when class executes
    componentDidMount() {
        axios.get('http://localhost:5000/browse/browse')
            .then(response => {
                this.setState({ results: response.data })
                // console.log(se.username)
            })
            .catch((error) => {
                console.log(error)
            })

        
    }

    //render method to display front end content

    render() {
        return (    
            <div>
                <div className="box-browse">
                    <form onSubmit={this.onSubmit}>
                        <div className='browse-border'>
                            <div className="line1">
                                <div className="item-1">
                                    <img className="browse-image" src={BusinessImg} style={{ WebkitBorderRadius: '22px' }} alt="Business"></img>
                                    <FormControlLabel className='browse-item-text' value="business" control={<Radio />} label="Business" onChange={this.onPriceChange.bind(this, 0)} />

                                </div>
                                <div className="item-2">
                                    <img className="browse-image" src={SpaceImg} style={{ WebkitBorderRadius: '22px' }} alt="Space"></img>
                                    <FormControlLabel className='browse-item-text' value="space" control={<Radio />} label="Space" onChange={this.onPriceChange.bind(this, 1)} />

                                </div><div className="item-3">
                                    <img className="browse-image" src={EnterTainmentImg} style={{ WebkitBorderRadius: '22px' }} alt="Entertainment"></img>
                                    <FormControlLabel className='browse-item-text' value="entertainment" control={<Radio />} label="Entertainment" onChange={this.onPriceChange.bind(this, 2)} />

                                </div>
                            </div>
                            <div className="line2">
                                <div className="item-1">
                                    <img className="browse-image" src={SportstImg} style={{ WebkitBorderRadius: '22px' }} alt="Business"></img>
                                    <FormControlLabel className='browse-item-text' value="sports" control={<Radio />} label="Sports" onChange={this.onPriceChange.bind(this, 3)} />


                                </div>
                                <div className="item-2">
                                    <img className="browse-image" src={PoliticsImg} style={{ WebkitBorderRadius: '22px' }} alt="Space"></img>
                                    <FormControlLabel className='browse-item-text' value="politics" control={<Radio />} label="Politics" onChange={this.onPriceChange.bind(this, 4)} />

                                </div><div className="item-3">
                                    <img className="browse-image" src={HealthImg} style={{ WebkitBorderRadius: '22px' }} alt="Entertainment"></img>
                                    <FormControlLabel className='browse-item-text' value="health" control={<Radio />} label="Health" onChange={this.onPriceChange.bind(this, 5)} />

                                </div>
                            </div>
                            <br></br>
                            <div className="line3">
                                <div className="item-1">

                                    <Button variant="contained" color="secondary" onClick={e => this.onSubmit(e)} style={{width:'100px', height:'40px'}}>
                                        OK
                                 </Button>

                                </div>
                            </div>

                        </div>
                    </form>

                </div>




            </div>
        );
    }
}
export default BankForm