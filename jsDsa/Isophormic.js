function isophormic(str1,str2){
    if(str1.length!== str2.length) return false
    let map1={}
    let map2={}
    for(let i=0;i<str1.length;i++){
        let ch1=str1[i]
        let ch2=str2[i]
        if((map1[ch1] && map1[ch1]!==ch2) || map2[ch2] && map2[ch2]!==ch1){
            return false
        }
        map1[ch1]=ch2
        map2[ch2]=ch1
    }
    return true
}
console.log(isophormic("egg","add"))
