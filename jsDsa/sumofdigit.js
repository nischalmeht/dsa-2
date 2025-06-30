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
    return digit
}
console.log(sumOfDigit(1345))