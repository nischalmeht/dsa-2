function maxSubarray(arr,k){
    if (arr.length<k) return null;
    let maxSum=0
    let winSum=0
    for(let i=0;i<k;i++){
        winSum+=arr[i]
    }
    maxSum=winSum
    for(let i=k;i<arr.length;i++){
        winSum+=arr[i] - arr[i-k]
        maxSum=Math.max(winSum,maxSum)
    }
    return maxSum
}
console.log(maxSubarray([2,1,5,1,3,2],3))
console.log(maxSubarray([1,9,2,4,5,6],2))