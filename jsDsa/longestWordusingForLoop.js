function longestWordusingForLoop(str){
    let string3= str.split(" ")
    let longestWord="";
    for( let i=0; i<string3.length; i++){
        if(string3[i].length> longestWord.length){
            longestWord= string3[i]
        }
    }
    return longestWord;
}
const string1= "Welcome to javascript guidesssssssssssssssssss";
console.log(longestWordusingForLoop(string1))