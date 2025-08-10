function createPerson(name,age){
    let privateName=name;
    let privateAge=age;
    function isAdult(){
        return age>=18
    }
    return {
        getName : function(){
            return privateName;
        },
        getAge : function(){
            return privateAge
        },
        setName : function(name){
            privateName = name
        },
        setAge : function(age){
            privateAge = age;
        },
        isAdult : isAdult
    }
}

let person = createPerson('Bittu',21)
console.log(person.privateAge) //undefined as not allowed to access private variable
console.log(person.getName());  // Bittu
console.log(person.getAge());   // 21
console.log(person.isAdult());  // true
