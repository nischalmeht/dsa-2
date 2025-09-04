// function substring(s,index,current=""){
//     // let res=[]
//     // for(let i=0;i<str.length;i++){
//     //     for(let j=i+1;j<=str.length;j++){
//     //         res.push(str.slice(i,j))
//     //     }
//     // }
//     // return res
//     if(index==s.length){
//         console.log(current)
//         return
//     }
//     substring(s,index+1,current+ s[index])
//     substring(s,index+1,current)

// }
function substring(s, index, current = "") {
    if (index == s.length) {
        console.log(current)
        return
    }
    substring(s, index + 1, current + s[index]) // include current char
    substring(s, index + 1, current)           // exclude current char
}
console.log(substring("abc"))