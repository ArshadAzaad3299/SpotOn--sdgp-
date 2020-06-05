import React from 'react';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import { Link } from 'react-router-dom';
import SearchRoundedIcon from '@material-ui/icons/SearchRounded';
import ListAltRoundedIcon from '@material-ui/icons/ListAltRounded';
import EqualizerRoundedIcon from '@material-ui/icons/EqualizerRounded';

//This class contains the Navigation bar which is used in All Windows

//material UI Constant for styles
const StyledTabs = withStyles({
  indicator: {
    display: 'flex ',
    height: 3,
    justifyContent: 'center',
    backgroundColor: 'transparent',
    '& > div': {
      maxWidth: '100%',
      width: '100%',
      backgroundColor: '#FCB415',

    },
  },
})((props) => <Tabs {...props} TabIndicatorProps={{ children: <div /> }} />);

const StyledTab = withStyles((theme) => ({
  root: {
    textTransform: 'none',
    color: '#fff',
    fontFamily: "Arial",
    letterSpacing: '2px',
    border: '#979595 dotted  1px',

    borderLeft: 'none',
    borderTop: 'none',
    borderBottom: 'none',
    fontWeight: theme.typography.fontWeightRegular,
    fontSize: theme.typography.pxToRem(15),
    marginRight: theme.spacing(1),
    '&:focus': {
      opacity: 1,
    },
  },
}))((props) => <Tab disableRipple {...props} />);

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  padding: {
    padding: theme.spacing(3),
  },
  demo2: {
    backgroundColor: '#2E2A2A',

  },
}));


//Functional Component which returns the Navigation Bar
export default function CustomizedTabs() {

  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const SearchName = (<div><SearchRoundedIcon className="navbar-text" />
    SEARCH</div>

  )
  const Topname = (<div><EqualizerRoundedIcon className="navbar-text" />
  TOP</div>

  )


  const BrowseName = (<div><ListAltRoundedIcon className="navbar-text" />BROWSE</div>)


  return (
    <div className={classes.root}>

      <div className={classes.demo2}>
        <nav>
          <StyledTabs value={value} onChange={handleChange} aria-label="styled tabs example" centered >
            <StyledTab label={SearchName} to='/spoton' component={Link} ></StyledTab>
            <StyledTab label={BrowseName} to='/spoton/browse' component={Link} />
            <StyledTab label={Topname} to='/spoton/top/load' component={Link} />
          </StyledTabs>
        </nav>
      </div>

    </div>
  );
}
