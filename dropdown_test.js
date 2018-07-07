var month_list = ["2010-12", "2011-03", "2011-06", "2011-09", "2011-12", "2012-03", "2012-06", "2012-09", "2012-12", "2013-03", "2013-06", "2013-09", "2013-12", "2014-03", "2014-06", "2014-09", "2014-12", "2015-03", "2015-06", "2015-09", "2015-12", "2016-03", "2016-06", "2016-09", "2016-12", "2017-03", "2017-06", "2017-09", "2017-12", "2018-03"];

var populate_dropdown = d3.select("body").selectAll("#date-selector").selectAll("option").data(month_list).enter().append("option").text(function(d) {
	return d;
});

var dd_value = d3.select("#date-selector").node().value; 

console.log(dd_value);

document.getElementById("date-selector").addEventListener("change", function() {
	dd_value = d3.select("#date-selector").node().value;
	console.log(dd_value);
}, false);
