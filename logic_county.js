// Creating map object
var map = L.map("map", {
  center: [37.752361, -122.080389],
  zoom: 9
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1IjoiYnVtYmFsb3JkIiwiYSI6ImNqaWNhZ2d1bjAxOHoza3BqcDQzMHR3Z3AifQ.KzBDaZozIdwa38NsQZslfw").addTo(map);

// var link = "http://data.beta.nyc//dataset/0ff93d2d-90ba-457c-9f7e-39e47bf2ac5f/resource/" +
// "35dd04fb-81b3-479b-a074-a27a37888ce7/download/d085e2f8d0b54d4590b1e7d1f35594c1pediacitiesnycneighborhoods.geojson";
// var link = "BayAreaCounties.geojson"
// Grabbing our GeoJSON data..
d3.json('BayAreaCounties.geojson', function(data) {
  // Creating a GeoJSON layer with the retrieved data
  L.geoJson(data).addTo(map);
});

// var geojsonLayer = new L.GeoJSON.AJAX("BayAreaCounties.geojson");       
// geojsonLayer.addTo(map);