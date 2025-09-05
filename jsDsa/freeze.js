function ObjectFreeze(obj){
    Object.freeze(obj)
    Object.keys(obj).forEach(key=>{
        if(typeof obj[key]==='object' && obj[key]!==null){
            ObjectFreeze(obj[key])
        }
    })
    return obj
}
let user= ObjectFreeze({name:"John",address:{city:"New York"}})
user.name="Jane"
user.address.city="Los Angeles"
console.log(user)
