// functional 
function Person(name, age, profession) {
  this.name = name;
  this.age = age;
  this.profession = profession;
}

Person.prototype.greeting = function () {
  console.log(`hi! ${this.name}`);
}

function Teacher(name, age, profession) {
  Person.call(this, name, age, profession);
  this.salary = "2000";
}

Teacher.prototype = Object.create(Person.prototype)
const teacherObj = new Teacher('anchal', 25, 'teacher');

Object.defineProperty(Teacher.prototype, 'constructor', {
  value: Teacher,
  enumerable: false,
  writable: true
})
console.log(teacherObj.name, Teacher.prototype.constructor)


class Person {
	constructor(name, age, profession) {
  	this.name = name;
    this.age = age;
    this.profession = profession;
  }
  greeting() {
  	return this.name;
  }
}
//  es6
class Teacher extends Person {
constructor(name, age, profession) {
		super(name, age, profession)
  }
}


const teacherObj = new Teacher('anchal', 25, 'artist');
console.log(teacherObj.name, teacherObj.profession, teacherObj.age, teacherObj.greeting())
