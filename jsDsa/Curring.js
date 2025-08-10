
function add(a){
	return function(b){
  	if(b !== undefined){
    	return add(a+b)
    }
  	return a;
  }
}

console.log(add(2)(4)()); 
function noofdigit(n){
    let num = Math.abs(n)
    let count=0
    do{
        count+=1
        n=Math.floor(n/10)
    }while(n>0)
     return count
}
console.log(noofdigit(123344))