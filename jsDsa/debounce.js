
const myFunction = function (event) {
    console.log(event.target.value);
    fetch(`https://api.github.com/users/${event.target.value}`)
      .then((response) => response.json())
      .then((data) => console.log("success", data));
  };
  
function debounce(func,delay){
    let timer ;
    return function(...args){
        clearTimeout(timer)
        timer=setTimeout(()=>{
            func(...args)
        },delay)
    }
}