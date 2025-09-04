function maxDepth(arr) {
    if (!Array.isArray(arr)) return 0; 
    let depth = 1; 
    for (let item of arr) {
        if (Array.isArray(item)) {
            depth = Math.max(depth, 1 + maxDepth(item));
        }
    }
    return depth;
}

console.log(maxDepth([1, [2, [3, [4]]]])); // 4
console.log(maxDepth([1, 2, [3, 4], 5]));  // 2
