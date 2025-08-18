function dosomething() {
// this is a normal function 
}

const dosomethingelse = ()=> {
    // this is an arrow function
}

export default function dosomething2() {
    // this is a default export function
}

export const someFunction = () => {
    // this is a named export function
}

const Mycomponet = () => {
    // this is a functional component
    return <div>My Component</div>
}

<button onClick= {() => console.log("hello world")
} ></button>; // this is anonymous function

let age1 = 25;
let name1 = age > 25 && "Ragul" // this is a short if true statement
let name2 = age > 25 || "Ragul" // this is a short if false statement
let name3 = age > 25 ? "Ragul" : "vishnu" // this is a short if else statement

// this is a simple object
const person = {
    name: "Ragul",
    age: 25,
    ismarried: false,
}

const { name , age, ismarried} = person; // this is object destructuring

const person2 = {...person, name: "Visgnu"} // this is object copying and updating

const name4 = ["Ragul","Vishnu", "sheron"];
const name5 = [...name4, "Jairus"] // this is array copying and updating
name4.map((name)=> {
    return name +  "1" ; // this is array map function
});

name4.map((name)=> {
    return <h1>{name}</h1>; // this is array map function with JSX
}); 

const names_list = ["Ragul","Vishnu","Ragul"]
name4.filter((name)=> {
    return name !== "Ragul" // this used to delete the name from the array
})


