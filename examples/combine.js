var myObject = {
    jsonOne: '',
    jsonTwo: ''
}
var combinedJSON;
d3.json("BayAreaCounties.geojson",function(data) {
   var newOb = data;
   console.log(newOb)
   myObject.jsonOne = newOb;
   d3.json("https://cors-anywhere.herokuapp.com/" + "ucb-dbc-project2.herokuapp.com/county_single_family", function(data) {
        var anotherObject = data;
        myObject.jsonTwo = anotherObject;
        // console.log(myObject)
        combinedJSON = JSON.stringify(myObject)
        // console.log(combinedJSON)
        myDisplayFunction(combinedJSON);
        console.log(Object.keys(combinedJSON))
   });
});

var myDisplayFunction = function(json){
    console.log(json.jsonOne)
    console.log(Object.keys(json))
}

console.log(combinedJSON)
// var myObject = {
//     json1: json1,
//     json2: json2,
// };
// var combinedJSON = JSON.stringify(myObject);

// console.log(combinedJSON)

// console.log(json1)