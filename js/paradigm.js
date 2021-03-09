const arr = [1,2,3]

/* imperative approach - how it is done- mutability, not pure functions*/
for(let i = 0; i< arr.length; i++) {
  arr[i] = arr[i]*2;
}

console.log(arr) 

/* declarative approach - what is done - immutability, pure functions*/
console.log(arr.map((element) => element*2))


function add (arr) {
  let result = 0
  for (let i = 0; i < arr.length; i++){
    result += arr[i]
  }
  return result
}
function add (arr) {
  return arr.reduce((prev, current) => prev + current, 0)
}

const arr = [1,2,3]

/* imperative approach - how it is done- mutability, not pure functions*/
const results = [];
for(let i = 0; i < arr.length; i++) {
	if(arr[i] % 2 === 0) {
  	results.push(arr[i])
  }
}

console.log(results)
/* declarative approach - what is done - immutability, pure functions*/
const isEven = (element) => element % 2 === 0;
console.log(arr.filter(isEven))
 

var people = [
  { name: "TK", age: 26 },
  { name: "Kaio", age: 10 },
  { name: "Kazumi", age: 30 }
];

var peopleSentences = [];

for (var i = 0; i < people.length; i++) {
  var sentence = people[i].name + " is " + people[i].age + " years old";
  peopleSentences.push(sentence);
}

console.log(peopleSentences); // ['TK is 26 years old', 'Kaio is 10 years old', 'Kazumi is 30 years old']

// In a declarative JavaScript way, it would be:
const makeSentence = (person) => `${person.name} is ${person.age} years old`;

const peopleSentences = (people) => people.map(makeSentence);
  
peopleSentences(people);
// ['TK is 26 years old', 'Kaio is 10 years old', 'Kazumi is 30 years old']