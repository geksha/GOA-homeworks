let date1 = new Date("2022-03-25");
let date2 = new Date("October 13, 2014 11:13:00"); 

function logDateProperties(date) {
    console.log("Full Year:", date.getFullYear());
    console.log("Month:", date.getMonth()); 
    console.log("Date:", date.getDate());
    console.log("Day of the Week:", date.getDay()); 
    console.log("Hours:", date.getHours());
    console.log("Minutes:", date.getMinutes());
    console.log("Seconds:", date.getSeconds());
    console.log("Milliseconds:", date.getMilliseconds());
}

console.log("Date 1 Properties:");
logDateProperties(date1);

console.log("Date 2 Properties:");
logDateProperties(date2);

