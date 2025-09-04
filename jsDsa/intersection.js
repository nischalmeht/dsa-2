function intersection(arr1,arr2){
    const set2=new Set(arr2);
    return [...new Set(arr1)].filter(item=>set2.has(item))
}
console.log(intersection([1,2,2,3],[2,3,4]))    