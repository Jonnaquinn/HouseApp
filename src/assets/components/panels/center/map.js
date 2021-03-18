import React, { useEffect } from 'react';
import L from 'leaflet';

function Map() {
  useEffect(() => {
    // create map
    L.map('map', {
      center: [49.8419, 24.0315],
      zoom: 16,
      layers: [
        L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
          attribution:
            '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        }),
      ]
    });
  }, []);

  return <div id="map"></div>
}

export default Map;