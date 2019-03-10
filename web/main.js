var date = [];
var speedUp = [];
var speedDown = [];
var coords = [];
let url = 'http://localhost:8080';



function makeMap() {
    var map = L.map('map').setView([13.5, 52.5], 2);



    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(map);

    for (var i in coords, date, speedDown, speedDown){
        text = "<strong>" +coords[i][2]+"</strong><br>" + new Date(date[i]) + "<br>down: "+ speedDown[i] +  " Mbit/s<br>up: " + speedUp[i] +  " Mbit/s"

        L.marker([coords[i][0], coords[i][1]]).addTo(map)
            .bindPopup(text)
            .openPopup();

    }


}

function plotTests() {

    plot = document.getElementById('plot');


    var trace1 = {
        x: date,
        y: speedDown,
        name: 'download',
        type: 'scatter'
    };

    var trace2 = {
        x: date,
        y: speedUp,
        name: 'upload',
        type: 'scatter'
    };

    var values = [trace1, trace2];

    var layout = {
        title: "Speed-Tests",
        yaxis: {
            title: 'Mbit/s',
            titlefont: {color: 'rgb(148, 103, 189)'},
            tickfont: {color: 'rgb(148, 103, 189)'},
            overlaying: 'y',
            side: 'left'
        }
    };

    Plotly.newPlot('plot', values, layout);




}


function getTests(){

    return $.getJSON(url).then(function(data){

        for (let i in data){
            speedDown.push(data[i][1]);
            speedUp.push(data[i][2]);
            date.push(data[i][9]);

            let coord = [data[i][4], data[i][5], data[i][8]];
            coords.push(coord);

        }

        plotTests();
        makeMap();




    });
}


getTests()



