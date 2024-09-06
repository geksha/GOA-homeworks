// function manualSlice(array, startindex,endindex) {
//     const listn = [];
//     for(let i = array; startindex < endindex; i++)
//         listn.push(i)
// }

function manualSlice(arr,start,end){
    let slicedArr = new Array();
    for(let i = start; i < end; i++){
        slicedArr.push(arr[i]);
    }

    console.log(slicedArr)
}
