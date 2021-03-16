import React, {useState, useEffect } from 'react';
import City from "../../../images/city.jpg"

export default function RightPanel(testing = false) {
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