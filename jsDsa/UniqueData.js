function unique(arr,key){
    let keyvalue= arr.map(item=>item[key])
    const val=[...new Set(keyvalue)]
    return val
}
const user = [
    { 'name': "nischal", "role": "employee" },
    { 'name': "nischal", "role": "admin" },
    { 'name': "nischal", "role": "viewer" },
    { 'name': "nischal", "role": "employee" },
    { 'name': "john", "role": "employee" },
  ];
  
  function uniqueData(arr,key){
    const seen=new Set()
    return arr.filter((item)=>{
        if(seen.has(item[key])) return false
        seen.add(item[key])
        return true
    })

  }
  console.log(unique(user, "role"));
  console.log(uniqueData(user, "name"));