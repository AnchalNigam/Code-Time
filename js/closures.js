const updateClickCount = (() => {
	let counter = 0;
  return () => {
    ++counter;
  	document.getElementById("spnCount").innerHTML = counter;
  }
})()


// html

// <button onclick="updateClickCount()">click me</button>
// <div> you've clicked
//     <span id="spnCount"> 0 </span> times!
// </div>

var library = (() => {
	const baseSalary = 18000;
	const calculateSalary = (employee) => {
  	return baseSalary + employee;
  }
	return {
  	calculateSalary: calculateSalary
  }
})()

console.log(library.calculateSalary(1000))
console.log(library.baseSalary)