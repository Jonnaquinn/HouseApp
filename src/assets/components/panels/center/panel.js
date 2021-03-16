import React, {useState, useEffect } from 'react';

export default function CenterPanel(testing = false) {

    // const [initalData, setInitialData] = useState([{}])
    // useEffect(() => {
    //     fetch('/api').then(
    //     response => response.json()
    //     ).then(data => setInitialData(data))
    // }, []);
    return (
        <div 
        id="panel.center"
        className="panel center">
            <div className="not-set">
                <h1 className="title">Please Fill Out Left Panel</h1>
                <p className="description">
                    To view all listed results, please first complete the form from the left hand panel.
                    After completing the form, this panel will populate with a map populated by your results.
                    This map will let you select property results and show more information for each properly listing.
                </p>
            </div>
        </div>
    );
}