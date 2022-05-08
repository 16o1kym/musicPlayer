import React, {useState} from 'react'
import Typography from '@material-ui/core/Typography';
import Radio from '@material-ui/core/Radio';
import { FormControl, FormLabel, FormControlLabel, RadioGroup , TextField , Button} from '@material-ui/core';

const createRoomPage = ()=>{

  const [canSkip , setCanSkip] = useState(true);
  const [votesToSkip , setVotesToSkip] = useState(2);



  const handleCanSkip = (bool) => {
    setCanSkip (bool)
  }

  const handleSetVotesToChange = (e) =>{ 
    setVotesToSkip(e.target.value);
  }

  const handleCreateRoom = () =>{
    console.log(votesToSkip, canSkip)
    const requestOptions = {
      method : 'POST',
      headers : {
        "Content-Type" : "application/json" 
      },

      body : JSON.stringify({
        votesToSkip : votesToSkip,
        guestCanPause : canSkip,
      })
    };
    
    fetch("/api/createRoom/" , requestOptions).then((response) =>
      response.json()).then((data) => console.log(data));
  }

  return (
    
    <>
    <Typography color = "primary" variant = "h2" align = "center">
      Create Room
    </Typography>

    <FormControl component="fieldset" >
  <FormLabel component="legend"> Guest can pause?</FormLabel>
  <RadioGroup aria-label=" Guest can pause?" name="pause" 
  // value={value} onChange={handleChange}
  >
    <FormControlLabel value="yes" control={<Radio onClick={()=> handleCanSkip (true) }/>} label="Yes" />
    <FormControlLabel value="no" control={<Radio onClick={()=>handleCanSkip (false)}/>} label="No" />
  </RadioGroup>
</FormControl>

<TextField id="standard-full-width" label="Votes to skip" onChange={handleSetVotesToChange}/>

<Button color='primary' variant='outlined' onClick={handleCreateRoom}>Create Room</Button>
    </>
  )
}

export default createRoomPage