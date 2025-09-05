function curry(func){
    return function curried(...args){
        if(args.length>=func.length){
            return func(...args)
        }else{
            return  (...next)=>curried(...args,...next)
        }
    }
}
function multiply(a,b,c,d){
    return a * b*c *d
}
const curried= currying(multiply)
console.log(curried(1)(2)(3)(0))