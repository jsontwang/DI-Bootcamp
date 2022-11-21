// Exercise 1 : Is_Blank
// Instructions
// Write a program to check whether a string is blank or not.

// console.log(isBlank('')); --> true
// console.log(isBlank('abc')); --> false


function isBlank(str){
  return /\s/.test(str);
}

console.log(isBlank(' ')); // --> true
console.log(isBlank('abc')); //--> false





// Exercise 2 : Abbrev_name
// Instructions
// Write a JavaScript function to convert a string into an abbreviated form.

// console.log(abbrevName("Robin Singh")); --> "Robin S."

//"Robin Singh"

function abbrevName(str){
  var splitStr = str.split(" ");
  return (`${splitStr[0]} ${splitStr[1].charAt(0)}.`)
}


abbrevName("Robin Singh")







// Exercise 3 : SwapCase
// Instructions
// Write a JavaScript function which takes a string as an argument and swaps the case of each character.
// For example :

// if you input 'The Quick Brown Fox' 
// the output should be 'tHE qUICK bROWN fOX'.

function SwapCase(str){
  let newStr = "";
  for(let value of str){
    let char = String(value);
    // console.log(char)
    char == char.toLowerCase() ? char = char.toUpperCase() 
    : char = char.toLowerCase();
    newStr+= char;
  }
  return newStr
}


SwapCase("The Quick Brown Fox")




// Exercise 4 : Omnipresent Value
// Instructions
// Create a function that determines whether an argument is omnipresent for a given array.
// A value is omnipresent if it exists in every subarray inside the main array.
// To illustrate:

// [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// // 3 exists in every element inside this array, so is omnipresent.
// Examples

// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false


function isOmnipresent(arr,value){
  // let value = arr[0][0];
  for (let i =0;i<arr.length;i++){
    console.log(`SubArray ${i}: ${arr[i]}`);
    for (let j =0;j<arr[i].length;j++){
      console.log(`element ${j}: ${arr[i][j]}`);
      // return (arr[i][j])
      if(!arr[i].includes(value)){
        return false
      }
  }
}
return true
}
