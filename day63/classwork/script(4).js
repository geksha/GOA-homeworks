// function start_Interval() {
//     let intervalId = setInterval(() => {
//         let now = new Date();
        
//         let currentMin = now.getMinutes();
        
//         console.log(now.toString());
        
//         if (currentMin === 35) {
//             clearInterval(intervalId);
//             console.log("Interval stopped at 35 minute");
//         }
//     }, 1000);
// }

// start_Interval();

let date = 0;
setInterval(function(){
    date ++;
    console.log("Current minutes are " + date);
    if(date === 34){
        console.log("Time up");
        clearInterval();
    }
    
},60000)

