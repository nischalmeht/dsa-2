const input={
    name:"Nischal",
    address:{
        city:"delhi",
        location:{
            lat:"10.55",
            long:"30.55",
        }
    }
}
function flattenObj(obj,parentkey="",result={}){
    for (let key in obj){
        const newKey=parentkey ? `${parentkey}.${key}`:key;
        if(typeof obj[key]==='object' && obj[key]!==null && !Array.isArray(obj[key])){
            flattenObj(obj[key],newKey,result)
        }else{
            result[newKey]=obj[key]
        }
    }
    return result

}
console.log(flattenObj(input))