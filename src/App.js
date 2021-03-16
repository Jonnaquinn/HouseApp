import React, {useState, useEffect } from 'react';
import "./assets/sass/base.scss";
// import './App.css';
import LeftPanel from "./assets/components/panels/left/panel";
import CenterPanel from "./assets/components/panels/center/panel";
import RightPanel from "./assets/components/panels/right/panel";

function App() {
  // const [initalData, setInitialData] = useState([{}])
  // const [currentTime, setCurrentTime] = useState(0);
  // useEffect(() => {
  //   fetch('/api').then(
  //     response => response.json()
  //   ).then(data => setInitialData(data))
  // }, []);

  // useEffect(() => {
  //   fetch('/time').then(res => res.json()).then(data => {
  //     setCurrentTime(data.time);
  //   })
  // }, []);

    return (
          <div className="App">
                <LeftPanel></LeftPanel>
                <CenterPanel></CenterPanel>
                <RightPanel></RightPanel>
              {/* {windowWidth} x {windowHeight} */}
              {/* {routes} */}
          </div>
    );


  // return (
  //   <div className="App">
  //     <h1 style={{color: 'white'}}>{initalData.title}</h1>
  //     {/* <img src={logo} className="App-logo" alt="logo" />
  //     <label for="to" style={{color: 'white'}}>From: </label>
  //     <input type="text" id="price-from" name="price-from"></input>
  //     <br></br>
  //     <label for="from" style={{color: 'white'}}>To: </label>
  //     <input type="text" id="price-to" name="price-to"></input>
  //     <br></br>
  //     <button onClick={() => {
  //       console.log(document.getElementById("price-from").value) 
  //       console.log(document.getElementById("price-to").value)
  //       }}>Scrape</button> */}
  //   </div>
  // );

  // return (
  //   <div className="App">
  //     <header className="App-header">
  //       <img src={logo} className="App-logo" alt="logo" />
  //       <p>
  //         Edit <code>src/App.js</code> and save to reload.
  //       </p>
  //       <a
  //         className="App-link"
  //         href="https://reactjs.org"
  //         target="_blank"
  //         rel="noopener noreferrer"
  //       >
  //         Learn React
  //       </a>
  //       <p>The current time is {currentTime}.</p>
  //     </header>
  //   </div>
  // );
}

export default App;
