function countNumberOfDigits(n){
    let num = Math.abs(n)
    // console.log(num)
    let count=0;
    do{
        count++
        num= Math.floor(num/10);
    }while (num>0)
    return count
}
console.log(countNumberOfDigits(12358))