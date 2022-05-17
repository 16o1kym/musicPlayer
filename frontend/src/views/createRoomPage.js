import React, {useState} from 'react'
import Typography from '@material-ui/core/Typography';
import Radio from '@material-ui/core/Radio';
import { FormControl, FormLabel, FormControlLabel, RadioGroup , TextField , Button} from '@material-ui/core';
import { useNavigate } from 'react-router-dom';


const createRoomPage = ()=>{

  const [canSkip , setCanSkip] = useState(true);
  const [votesToSkip , setVotesToSkip] = useState(2);
  // const [CSRFToken , setCSRFToken] = useState("");
  const nav = useNavigate();


  const handleCanSkip = (bool) => {
    setCanSkip (bool)
  }

  const handleSetVotesToChange = (e) =>{ 
    setVotesToSkip(e.target.value);
  }

  const getCSRFToken = async () =>{
    try{
      const res = await fetch("/api/");
      const data = await res.json();
      return data;
    } catch(err){
      console.log(err);
    }
    return "";
  }
  
  const handleCreateRoom = async () =>{
    const csrf = await getCSRFToken();
    console.log(csrf)
    console.log(votesToSkip, canSkip)
    const requestOptions = {
      method : 'POST',
      headers : {
        "Content-Type" : "application/json" ,
        "X-Csrftoken" : csrf,
      },
      body : JSON.stringify({
        votesToSkip : votesToSkip,
        guestCanPause : canSkip,
      })
    };
    
    const res = await fetch("/api/createRoom/" , requestOptions);
    const data = await res.json();
    console.table(data);
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
    <FormControlLabel value="yes" control={<Radio onClick={()=> handleCanSkip (true) }/>} label="Play/Pause" />
    <FormControlLabel value="no" control={<Radio onClick={()=>handleCanSkip (false)}/>} label="No Control" />
  </RadioGroup>
</FormControl>

<TextField id="standard-full-width" label="Votes to skip" onChange={handleSetVotesToChange}/>

<Button color='primary' variant='outlined' onClick={handleCreateRoom}>Create Room</Button>
    </>
  )
}

export default createRoomPage