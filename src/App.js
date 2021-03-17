import React, {useState, useEffect } from 'react';
import "./assets/sass/base.scss";
// import './App.css';
import LeftPanel from "./assets/components/panels/left/panel";
import CenterPanel from "./assets/components/panels/center/panel";
import RightPanel from "./assets/components/panels/right/panel";
import { ManagerProvider } from "./assets/components/hooks/useManagerStore";


function App() {
    return (
      <ManagerProvider>
          <div className="App">
                <LeftPanel></LeftPanel>
                <CenterPanel></CenterPanel>
                <RightPanel></RightPanel>
          </div>
      </ManagerProvider>
    );
}

export default App;
