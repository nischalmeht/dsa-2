function subsequence(s1,s2){
    let i=0
    let j=0
    while (i<s1.length && j<s2.length){
        if(s1[i]==s2[j]){
            i+=1
        }
        j++
    }
    return i==s1.length
}
console.log(subsequence("abc","ahbgdc"))