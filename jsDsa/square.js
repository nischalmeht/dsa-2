console.log(sumOfSquares([1, 2, 3, 4, 5])); 
function sumOfSquares(arr){
    const squares=arr.map((num)=>num **2)
    return squares.reduce((sum,square)=>sum + square,0)
}
function* lazySquare(arr){
    for(let num of arr){
        yield num**2
    }
}
function sumOfSquares(arr){
    let sum=0;
    for(const square of lazySquare(arr)){
        sum+=square
    }
    return sum
}
console.log(sumOfSquares([1, 2, 3, 4, 5]))
// onsole.log(25+16+9+4+1)