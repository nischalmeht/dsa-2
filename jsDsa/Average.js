// Sample data structure for all questions
const schoolData = [
    {
      class: "Math",
      students: [
        { name: "Alice", grade: 90, activities: ["Chess", "Debate"] },
        { name: "Bob", grade: 80, activities: ["Soccer", "Debate"] },
      ],
    },
    {
      class: "Science",
      students: [
        { name: "Charlie", grade: 85, activities: ["Chess", "Drama"] },
        { name: "Diana", grade: 95, activities: ["Soccer", "Drama"] },
      ],
    },
  ];
function calculateArray(schoolData){
    return schoolData.map((classData)=>{
        return{
            class:classData.class,
            grade:classData.students.map((item)=>item.grade).reduce((a,b)=>a+b)/classData.students.length
        }
    })
}  

console.log(calculateArray(schoolData))