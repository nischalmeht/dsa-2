function difference(arr1,arr2){
    const set1=new Set(arr2);
    return arr1.filter((item)=>set1.has(item))
}
console.log(difference([1,2,3,4],[1,2,4]))