function add(num1,num2){
    return num1 + num2
}
function createSumCache(){
    const cache={};
    return function(num1,num2){
        const key= num1 + "+" + num2;
        console.log(key,"cache");
        if(cache.hasOwnProperty(key)){
            console.log("return from cache")
            return cache[key]
        }else{
            console.log("calculating sum ...");
            const sum = add(num1,num2);
            cache[key]=sum;            
            return sum
        }

    }    
}
const sumCache= createSumCache();
console.log(sumCache(2,3))
console.log(sumCache(2,3))
console.log(sumCache(5,3))
console.log(sumCache(5,3))
