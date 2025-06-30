const arr=[
    {
      "name": "John Doe",
      "city": "New York",
      "age": 30
    },
    {
      "name": "Alice Smith",
      "city": "Los Angeles",
      "age": 25
    },
    {
      "name": "Raj Mehta",
      "city": "Mumbai",
      "age": 28
    }
  ]

  function groupArray(arr,products){  
   return arr.reduce((acc,item)=>{
    if (!acc[item[products]]){
        acc[item[products]]=[]
    }
    acc[item[products]].push(item)
    return acc

    },{})
  }
  console.log(groupArray(arr,"city"))