// function convert(a){
//     const hours = Math.floor(a / 60);
//     const mins = a % 60;

//     console.log(`Часов: ${hours}, Минут: ${mins}`)
// }
// console.log(convert(243))

// // // // //

// var s = [10, 5, 9, -4, 2, -8]

// function tiposet(s){
//     var bolshe = []
//     for (var i of s){
//         if (i > 0){
//             bolshe.push(i)
//         }
//     }
//     return bolshe
// }
// console.log(tiposet(s))

// // // // //

// var pokupki = ["Свитер", "Галстук", "Ананас", "Туфли"]

// function poisk(pokupki, slovo){
//     var shet = 1
//     for (var i of pokupki){
//         if (i === slovo){
//             return `Да, это есть в наличии! Номер позиции ${shet}`
//         }
//         shet++
//     }
//     return "Объект не найден"
// }
// console.log(poisk(pokupki, "Туфли"))

// // // // //

// class scoreboard{
//     constructor (){
//         this.points = 0
//     }

//     add_points(points){
//         this.points += points
        
//         return this.points
//     }
       
//     del_points(points){
//         if (this.points < points){
//             this.points = 0
//         }
//         else{
//             this.points -= points
//         }
       
        
//         return this.points
//     }
       

    
// }
// var a = new scoreboard()
// console.log(a.add_points(8))
// console.log(a.del_points(9))

// // // // //


// var a = 5

// console.log(a + 5)


























// // // // //

// text = "Ты сам дуры ак"

// pattern = r"дурак|дура|дуры|дураки|зл|плох\w"
// text_2 = re.sub(pattern, "Хороший человек", text, flags=re.IGNORECASE)
// print(text_2)

const text_1 = "Ты дурак ха=ха"

const pattern = /дурак|дура|дуры|дураки|зл|плох\w*/gi

const text_2 = text_1.replace(pattern, "*")


console.log(text_2)






