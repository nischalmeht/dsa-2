function mergeObject(obj1,obj2){
    let result={}
    for(let key in obj1){
        if(obj1.hasOwnProperty(key)){
            result[key]=obj1[key]
        }
    }
    for(let key in obj2){
        if(obj2.hasOwnProperty(key)){
            result[key]=obj2[key]
        }
    }
    return result
}
console.log(mergeObject({a:1,b:2},{c:3,d:4}))