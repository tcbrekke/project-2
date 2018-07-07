month_list = ["2010-12", "2011-03", "2011-06", "2011-09", "2011-12", "2012-03", "2012-06", "2012-09", "2012-12", "2013-03", "2013-06", "2013-09", "2013-12", "2014-03", "2014-06", "2014-09", "2014-12", "2015-03", "2015-06", "2015-09", "2015-12", "2016-03", "2016-06", "2016-09", "2016-12", "2017-03", "2017-06", "2017-09", "2017-12", "2018-03"]

console.log(month_list);

var selector = d3.select("body")
  .append(select)
  .data(month_list)
  .attr("id", "date-selector")
  .selectAll("option")
  .enter().append("option")
  .text(function (item) {
    console.log(item);
    return item;
  });

selector();

var myObject = {
    jsonOne: '',
    jsonTwo: ''
}
var combinedJSON;
d3.json("BayAreaCounties.geojson",function(data) {
   var newOb = data;
   for (obj in newOb) {
      var checkCounty = obj.features.properties.county;
   }
   console.log(newOb)
   myObject.jsonOne = newOb;
   d3.json("https://cors-anywhere.herokuapp.com/" + "ucb-dbc-project2.herokuapp.com/county_single_family", function(data) {
        var anotherObject = data;
        for (obj in anotherObject) {
          if (obj.RegionName == checkCounty) {
            myObject.jsonTwo = anotherObject;
            combinedJSON = JSON.stringify(myObject);
          }
        }
        // console.log(combinedJSON)
        myDisplayFunction(combinedJSON);
        console.log(Object.keys(combinedJSON))
   });
});


d3.json("BayAreaCounties.geojson", function(data) {
  // Creating a geoJSON layer with the retrieved data

  geoJson = L.geoJson(data, {
    // Style for each feature (in this case a neighborhood)
    style: function(feature) {
      return {
        color: "white",
        // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
        fillColor: getColor(feature.properties.county),
        fillOpacity: 0.5,
        weight: 1.5
      };
    },
    // Called on each feature
    onEachFeature: function(feature, layer) {
      // Setting various mouse events to change style when different events occur
      layer.on({
        // On mouse over, make the feature (neighborhood) more visible
        mouseover: function(event) {
          layer = event.target;
          layer.setStyle({
            fillOpacity: 0.9
          });
        },
        // Set the features style back to the way it was
        mouseout: function(event) {
          geoJson.resetStyle(event.target);
        },
        // When a feature (neighborhood) is clicked, fit that feature to the screen
        click: function(event) {
          map.fitBounds(event.target.getBounds());
        }
      });
      d3.json("https://cors-anywhere.herokuapp.com/" + "ucb-dbc-project2.herokuapp.com/region_affordability", function(data) {
        for (thing in data) {
          if (thing.RegionName == feature.properties.county) {
            countyPrice = thing[`${input}`];
            break;
          }
          else {
            i++;
          }

        }
      }
      // Giving each feature a pop-up with information about that specific feature
      layer.bindPopup("<h2>" + feature.properties.county + "</h2><hr><h3>" + countyPrice + "</h3>");
    }
  }).addTo(map);
});