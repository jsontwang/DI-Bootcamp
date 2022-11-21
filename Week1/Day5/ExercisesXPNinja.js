// Exercise 1: Random Number
// Instructions
// Get a random number between 1 and 100.
// Console.log all even numbers from 0 to the random number.

let randomNum = Math.floor(Math.random() * 100) + 1;


function checkEvenRandom(randomNum){

  let evenNum ="";
  for (let i = 0;i<randomNum;i++){
    if(i%2 ===0){
      evenNum+= i + ","
    }
  }
  return (`Even number from 0 to ${randomNum}: ${evenNum}`)
}




// Exercise 2: Capitalized Letters
// Instructions
// Create a function that takes a string as an argument.
// Have the function return:
// The string but all letters in even indexes should be capitalized.
// The string but all letters in odd indexes should be capitalized.
// Note:

// Index 0 will be considered even.
// The argument of the function should be a lowercase string with no spaces.
// For example,

// capitalize("abcdef") will return ['AbCdEf', 'aBcDeF']

capitalString("abcdef")

function capitalString(str){
  let stringStr = String(str);
  let evenString= "";
  let oddString = "";
  evenString = evenStringConvertion(stringStr,evenString);
  oddString = oddStringConvertion(stringStr,oddString);
  console.log(`[${evenString} , ${oddString}]`)

}

function evenStringConvertion(str,evenString){
  for (let i in str){
    // console.log(i)
    if(isEven(i)){
      evenString+= str.charAt(i).toUpperCase()
    }else{
      evenString+=str.charAt(i)
    }
  }
  return evenString
}

function oddStringConvertion(str,oddString){
  for (let i in str){
    // console.log(i)
    if(!isEven(i)){
      oddString+= str.charAt(i).toUpperCase()
    }else{
      oddString+=str.charAt(i)
    }
  }
  return oddString
}

function isEven(index){
  return index%2===0 ? true:false
}



// Exercise 3 : Is Palindrome?
// Instructions
// Write a JavaScript function that checks whether a string is a palindrome or not.
// Note A palindrome is a word, phrase or sequence that is spelled the same both backwards and forward, e.g., madam, bob or kayak.
// palindrome

let str = "Madam"

function isPalindrome(str){
  let string = String(str.toLowerCase())
  // console.log(string)
  let arr = string.split("");
  // console.log(arr)
  let reverseArr = arr.reverse();
  // console.log(reverseArr)
  let reverseStr = reverseArr.join();
  // console.log(reverseStr)

  return (string === reverseStr) ? `${str} is a palindrome` : `${str} is  not a palindrome`;
}


// Exercise 4 : Biggest Number
// Instructions
// Create a function called biggestNumberInArray(arrayNumber) that takes an array as a parameter and returns the biggest number.
// Note : This function should work with any array;
// Example:

const array = [-1,0,3,100, 99, 2, 99] ;// should return 100 
const array2 = ['a', 3, 4, 2]; // should return 4 
const array3 = []; // should return 0


function biggestNumberInArray(arr){
  let biggestNumber = 0;
  for(let i =0;i<arr.length;i++){
    if(arr[i] > biggestNumber){
      biggestNumber = arr[i];
    }
  }
  return biggestNumber
}


// Exercise 5: Unique Elements
// Instructions
// Write a JS function that takes an array and returns a new array with only unique elements.

// Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]
// Example list=[1,2,3,3,3,3,4,5] newList = [1,2,3,4,5]


const list=[1,2,3,3,3,3,4,5];


function uniqueArray(list) {
  const tempArray = [];
  for (i of list){
    if(!tempArray.includes(i)){
      tempArray.push(i);
    }
  }
    return tempArray
}

uniqueArray(list)
  







