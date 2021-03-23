import React, {useState, useEffect } from 'react';
import City from "../../../images/city.jpg"
import logo from "../../../images/logo.svg"
import { useManager, UseManager, useManagerDispatch } from "../../hooks/useManagerStore"


export default function RightPanel(testing = false) {
    const { formSubmit, formClicked, iFrameClicked } = useManager();
    const managerDispatch = useManagerDispatch();
    let [state, setState] = React.useState({
        limit: "1000",
        radius: "",
        venuecategory: "",
      })
      function reset() {
        setState({
          limit: "",
          radius: "",
          venuecategory: "",
        })
      }
    function Buttons() {
    // do somthing
    
    return (
        <div className="panel-buttons">
            <div className="ok-button"
            onClick={() => {        
                console.log("ok button")
                console.log(JSON.stringify(state))
                handleSubmit();
                managerDispatch({ type: "submit", value: {formSubmit: true} })
                managerDispatch({ type: "submitClick" })
                // test1();
                // managerDispatch({ type: "iFrameClick", value: {iFrameClicked: true} })
            }}
        >
            Ok
            </div>
            <div className="cancel-button"
            onClick={() => {
                console.log("cancel button")
                // managerDispatch({ type: "submit", value: {formSubmit: false} })
                reset();
            }}
        >
            Clear
            </div>
        </div>
    )
    }
    function handleChange(e) {
        const value = e.target.value;
        setState({
        ...state,
        [e.target.name]: value
        });
        // console.log(e.target.name, value)
    }

    function handleSubmit() {
        fetch("/filter", {
          method: "POST",
          cache: "no-cache",
          headers: {
            "content_type":"application/json",
            'Accept': 'application/json'
          },
          body:JSON.stringify(state)
        })
      }

    if (formSubmit) {
        return (
            <div id="panel.right" className="panel right">
                <img src={logo} className="logo" alt="logo" />
                <div className="container">
                        <div>
                            <h1 className="title">Filter Listings</h1>
                            <p className="description">
                            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type.
                            </p>
                            <hr style={{marginTop: '17px', marginBottom: '17px'}}></hr>
                            <div className="TextInputHalfLeft">
                            <input placeholder="-- Limit --" type="text" autoComplete="none" name="limit" value={state.limit} onChange={handleChange}/>
                            </div>
                            <div className="TextInputHalfRight">
                            <input placeholder="-- Radius --" type="text" name="radius" value={state.radius} onChange={handleChange}/>
                        </div>
                        <div className="TextInput">
                            <input placeholder="-- Venue Category --" type="text" autoComplete="none" name="venuecategory" value={state.venuecategory} onChange={handleChange}/>
                        </div>
                        </div>
                    <Buttons></Buttons>
                </div>
            </div>
        )
    }
    return (  
            <div id="panel.right" className="panel right">
                <div className="not-set">
                    <div className="overlay">
                        <img src={City} alt="City" />
                    </div>
                </div>
            </div>
    );
}