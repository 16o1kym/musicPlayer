import React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router } from "react-router-dom";
 
import Routes from '../Routes/index'


const App = ()=>{
  return (
    <Router>
      {/* wraping with router bcoz to provide the functionality of router to this Routes */}
      <Routes/> 
    </Router>
   
  )
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);