function PowerSet(arr){
    let res=[[]]
    for(let char of arr){
        let newArray= res.map((item)=>[...item,char])
        res.push(...newArray)
    }
    return res
}
console.log(PowerSet([1,2,3]))