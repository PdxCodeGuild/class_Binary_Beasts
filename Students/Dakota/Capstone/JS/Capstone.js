// Display Leaflet Map
var mymap = L.map("Map").setView([30.332, -81.655], 13);

L.tileLayer(
  "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
  {
    maxZoom: 18,
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
      'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: "mapbox/streets-v11",
    tileSize: 512,
    zoomOffset: -1,
  }
).addTo(mymap);

// Display Gantt Chart
google.charts.load("current", {
  packages: ["gantt"],
});
google.charts.setOnLoadCallback(drawChart);

function daysToMilliseconds(days) {
  return days * 24 * 60 * 60 * 1000;
}

function drawChart() {
  var data = new google.visualization.DataTable();
  data.addColumn("string", "Task ID");
  data.addColumn("string", "Task Name");
  data.addColumn("date", "Start Date");
  data.addColumn("date", "End Date");
  data.addColumn("number", "Duration");
  data.addColumn("number", "Percent Complete");
  data.addColumn("string", "Dependencies");

  data.addRows([
    [
      "GISData",
      "Find Available GIS Data",
      new Date(2021, 5, 1),
      new Date(2021, 5, 4),
      null,
      100,
      null,
    ],
    [
      "ArcGISPro",
      "Compile Data within ArcGIS pro",
      null,
      new Date(2021, 5, 7),
      daysToMilliseconds(3),
      25,
      "GISData",
    ],
    [
      "ArcGISOnline",
      "Create ArcGIS Online Web Mapping Application",
      null,
      new Date(2021, 5, 8),
      daysToMilliseconds(1),
      20,
      "GISData,ArcGISPro",
    ],
    [
      "Test",
      "Test Web Mapping Application Funtionality",
      null,
      new Date(2021, 5, 10),
      daysToMilliseconds(1),
      0,
      "GISData,ArcGISOnline",
    ],
    [
      "QC",
      "QC Web Mapping Application Funtionality",
      null,
      new Date(2021, 5, 11),
      daysToMilliseconds(1),
      25,
      "GISData,Test",
    ],
    [
      "Complete",
      "Submit App to Client",
      null,
      new Date(2021, 5, 12),
      daysToMilliseconds(1),
      100,
      "GISData,QC",
    ],
  ]);

  var options = {
    height: 275,
  };

  var chart = new google.visualization.Gantt(
    document.getElementById("chart_div")
  );

  chart.draw(data, options);
}
