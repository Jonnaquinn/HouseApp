import React, {useState, useEffect } from 'react';
import logo from "../../../images/logo.svg"
import Form from "../../inputs/form"
import { UseManager, useManagerDispatch } from "../../hooks/useManagerStore"


// function Buttons() {
//     // do somthing

//     return (
//         <div className="panel-buttons">
//             <div className="ok-button"
//             onClick={() => {
//                 console.log("ok button")
//             }}
//         >
//             Ok
//             </div>
//             <div className="cancel-button"
//             onClick={() => {
//                 console.log("cancel button")
//             }}
//         >
//             Cancel
//             </div>
//         </div>
//     )
// }

export default function LeftPanel() {
    const managerDispatch = useManagerDispatch();
    return (  
            <div id="panel.left" className="panel left">
                <img src={logo} className="logo" alt="logo" />
                <div id="container" className="container">
                    <h1 className="title">search listings</h1>
                    <p className="description">
                    Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
                    Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type. 
                    </p>
                    <hr style={{marginTop: '15px'}}></hr>
                    <Form></Form>
                    {/* <Buttons></Buttons> */}
                </div>
            </div>
    );
}