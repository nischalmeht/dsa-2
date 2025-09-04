const data={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
}
function filterObject(obj,callback){
    return Object.fromEntries(Object.entries(obj).filter(([key,value])=>callback(value,key)))
}
console.log(filterObject(data,val=>val%2==0))
console.log(filterObject(data,val=>val>1))
