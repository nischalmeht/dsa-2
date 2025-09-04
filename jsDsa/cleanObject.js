function cleanObject(obj){
    let result={}
    for(let key in obj){        
        if(obj.hasOwnProperty(key) && obj.has(key)){
            result[key]=obj[key]
        }
    }
    return result

}
console.log(cleanObject({"name":"Durai","age":23,"city":"","isActive":true}))
console.log(cleanObject({"name":null,"age":undefined,"city":"js","isActive":true}))