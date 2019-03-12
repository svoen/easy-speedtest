let date = [];
let speedUp = [];
let speedDown = [];
let coords = [];
let sponsor = [];
let url = 'http://localhost:8040';



function makeMap() {
    var map = L.map('map').setView([13.5, 52.5], 2);



    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(map);


    popupText = "<strong>" +sponsor[coords.length - 1]+"</strong><br>" + new Date(date[date.length - 1]) + "<br>down: "+ speedDown[speedDown.length - 1] +  " Mbit/s<br>up: " + speedUp[speedUp.length - 1] +  " Mbit/s"

    L.marker([coords[coords.length - 1][0], coords[coords.length - 1][1]]).addTo(map)
        .bindPopup(popupText)
        .openPopup();

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


    return $.getJSON(url).then(function (data) {


        for (let i in data) {
            speedDown.push(data[i][1]);
            speedUp.push(data[i][2]);
            let coord = [data[i][4], data[i][5]];
            sponsor.push(data[i][8]);
            date.push(new Date(data[i][9]));
            coords.push(coord);

        }

        plotTests();
        makeMap();


    });

}


getTests()


$.getJSON(url, function() {
    alert("success");
}).error(function() { alert("error"); }).complete(function() { alert("complete"); });
