'use strict';
const btn = document.querySelector(".data-button")

btn.addEventListener('click', function(){
    var row = document.querySelector("#selected-row");
    var flightNumber = document.querySelector("#selected-row .flight-info1").textContent;
    var Airline = document.querySelector("#selected-row .flight-info2").textContent;
     var departureCity = document.querySelector("#selected-row .flight-info3").textContent;
    var arrivalCity = document.querySelector("#selected-row .flight-info4").textContent;
    var Time = document.querySelector("#selected-row .flight-info5").textContent;


    console.log(flightNumber, Airline,departureCity, arrivalCity, Time )
})