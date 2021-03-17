import React, {useState, useEffect } from 'react';
import { useManager, UseManager, useManagerDispatch } from "../../hooks/useManagerStore"

// import { UseManager, useManagerDispatch } from "../../hooks/useManagerStore"
// import Iframe from 'react-iframe';
export default function CenterPanel(testing = false) {
    const { formSubmit, formClicked } = useManager();
    const managerDispatch = useManagerDispatch();
    // React.useEffect(() => {
    // }, [formClicked]);
    return (
        <div 
        id="panel.center"
        className="panel center">
            {formSubmit ? (
                <div className="map">
                    <iframe key={formClicked} id="map" src="http://localhost:5000/" width="90%" height="35%"></iframe>
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