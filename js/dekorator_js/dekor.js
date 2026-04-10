// console.log("Начинаем работу")

// function grayting(){
//     console.log("Привет, " + "David")



// }

// function dekorator(funk){
//     return function(){
//         console.log("Смотри!");
//         funk();
//         console.log("Свершилось!");
//     };



// }

// grayting = dekorator(grayting)


// grayting()





// // // // // // // // // // // // // // // // // // // // // //

function time_dekorator(funk){
    return function(...args){
        const start = performance.now();
        funk(...args);
        const end = performance.now();
        console.log(`Время ${end - start}`)
    };
}

function calc(n){
    var sum = 0
    for (let i = 0; i < n; i++){
        sum = sum + i

    }
    

}

calc = time_dekorator(calc)
calc(10000000)