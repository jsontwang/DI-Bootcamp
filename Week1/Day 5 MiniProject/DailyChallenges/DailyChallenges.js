let maxBottle = 99;
let grammar ="is";
// let remainingBottle =0;

let number = Number(prompt("input a number: ",0))

console.log(`We start the song at 99 bottles`)
do {
    grammar = checkGrammar(number);
    if(number > maxBottle){
        number= maxBottle;
    }
    maxBottle = maxBottle - number;
    console.log(`Take ${number} down, pass ${grammar} around`)
    number+= 1;
    console.log(`we now have ${maxBottle} bottles`)
}while((maxBottle > 0))

  
function checkGrammar(number){
    if(number >1){
        grammar = "them" 
    }else{
        grammar = "it"
    }
    return grammar
}

// function promptBeer(grammar,maxBottle){
//     number = Number(prompt("input a number: ",0))
//     grammar = checkGrammar(number);
//     maxBottle = maxBottle - number;
//     console.log(maxBottle)
//     console.log(`Take ${number} down, pass ${grammar} around`)
//     console.log(`we now have ${maxBottle} bottles`)
// }
