// Creating map object
var map = L.map("map", {
  center: [37.752361, -122.080389],
  zoom: 9
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1IjoiamVzc2J1cmdvcyIsImEiOiJjamlkdm14dzEwNnZqM3BwbnA3a3ZmcXZ4In0.S_8R6Xa8awTcuIXPU7jexA").addTo(map);

// Grabbing our GeoJSON data..
d3.json('marin_county.geojson', function(data) {
  // Creating a GeoJSON layer with the retrieved data
  L.geoJson(data).addTo(map);
});

// var geojsonLayer = new L.GeoJSON.AJAX("BayAreaCounties.geojson");       
// geojsonLayer.addTo(map);