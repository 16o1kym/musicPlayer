import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'

export default function Room(props) {

    const { roomCode } = useParams();
    const [states, setState] = useState({
        votesToSkip: 0,
        guestCanPause: false,
        is_host: false,
    })

    useEffect(() => {
        getRoomDetails();
    }, []);
    const getRoomDetails = async () => {
      const res = await  fetch("/api/get-room?code=" + roomCode);
      const data = await res.json ();
      console.table(data);
      setState ({
          votesToSkip: data.votesToSkip,
          guestCanPause: data.guestCanPause,
          is_host: data.is_host
      })
    }
    return (
        <div>
            <h1>{roomCode}</h1>
            Room
            <h4>{states.votesToSkip.toString()}</h4>
            <h4>{states.guestCanPause.toString()}</h4>
        </div>
    )
}

// 'X-CSRFToken' : "abcde",