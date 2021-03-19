import React, {useState, useEffect } from 'react';
import { useManager, UseManager, useManagerDispatch } from "../../hooks/useManagerStore"
// import Map from "./map"
// import { UseManager, useManagerDispatch } from "../../hooks/useManagerStore"
// import Iframe from 'react-iframe';
export default function CenterPanel(testing = false) {
    const { formSubmit, formClicked, iFrameClicked } = useManager();
    const managerDispatch = useManagerDispatch();
    // React.useEffect(() => {
    // }, [formClicked]);
    // window.addEventListener('blur',function(){
    //     if(document.activeElement.id == 'map'){
    //         managerDispatch({ type: "iFrameClick", value: {formSubmit: true} })
    //         console.log('clicked')
    //     }
    // });
    function test() {
        // console.log('yo')
        if (document.getElementById("map")) {
            // console.log(document.getElementById("popup").textContent)
            console.log(document.getElementById('map').contentWindow.document.getElementById('popup'))
            console.log('yo12')
        }
    }
    return (
        <div 
        id="panel.center"
        className="panel center">
            {formSubmit ? (
                <div className="map">
                    {/* <Map style={{width: '10px'}}></Map> */}
                    <iframe sandbox="allow-forms allow-scripts allow-same-origin allow-downloads" key={formClicked} id="map" src="http://localhost:5000/domain_api" width="90%" height="35%"></iframe>
                </div>
            ) : (
                <div className="not-set">
                    <h1 className="title">Please Fill Out Left Panel</h1>
                    <p className="description">
                        To view all listed results, please first complete the form from the left hand panel.
                        After completing the form, this panel will populate with a map populated by your results.
                        This map will let you select property results and show more information for each properly listing.
                    </p>
                </div>
            )}
            {/* <Iframe
            src="http://localhost:5000/map"
            width="95%"
            height="36%"
            /> */}
            {/* <iframe src="http://localhost:5000/map" title="W3Schools Free Online Web Tutorials" width="90%" height="35%"></iframe> */}
            {/* <div className="not-set">
                <h1 className="title">Please Fill Out Left Panel</h1>
                <p className="description">
                    To view all listed results, please first complete the form from the left hand panel.
                    After completing the form, this panel will populate with a map populated by your results.
                    This map will let you select property results and show more information for each properly listing.
                </p>
            </div> */}
        </div>
    );
}