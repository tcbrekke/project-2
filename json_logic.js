county_single_family_url = "https://cors-anywhere.herokuapp.com/" + "ucb-dbc-project2.herokuapp.com/county_single_family"

function fetch_json(json_url) {
	var data = d3.json(json_url);
	return data;
} 

var country_sfr = fetch_json(county_single_family_url);

console.log(country_sfr)

// .then(function(data){
// 	console.log(data)
// }).catch(function(err){
// 	console.log(err)
// })

d3.json("https://cors-anywhere.herokuapp.com/" + "ucb-dbc-project2.herokuapp.com/county_single_family").then(function(data) { 
	console.log(data);
})