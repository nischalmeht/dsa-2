function sumOfDigit(n){
    let reminder;
    let sum=0
    let digit=""
    while(n>0){
        reminder = n%10;
        digit+=reminder
        sum=reminder + sum
        n=Math.floor(n/10)
    }
    return sum
}
// function sumOfDigit(n) {
//     if (n < 10) return n; // base case: single digit
//     const sum = n.toString().split("").reduce((acc, digit) => acc + parseInt(digit), 0);
//     return sumOfDigit(sum);
// }

console.log(sumOfDigit(1345)); // 4
