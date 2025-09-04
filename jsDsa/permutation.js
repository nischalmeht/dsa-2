str="abc"
function getPermutation(str){
    let res=[]
    for (let i=0;i<str.length; i++){
        let char=str[i]
        let newStr=str.slice(0,i) + str.slice(i+1)
        let substring=getPermutation(newStr)
        for(let item of substring){
            res.push(char + item)
        }
    }
    return res
}
console.log(getPermutation("abc"))