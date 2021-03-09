// map 
Array.prototype.myMap = function (callback) {
	const arr = this;
  if(!arr || !Array.isArray(arr)  || typeof callback !== 'function') {
  	return;
  }
  let result = [];
  for(let i = 0; i< arr.length; i++) {
  	result.push(callback(arr[i], i, arr));
  }
  
  return result;
}


console.log([].map((elem) => elem*2));
console.log([].myMap((elem) => elem*2));

// filter
Array.prototype.myFilter = function(callback) {
	const arr = this;
  if(!arr || typeof callback !== 'function' || Object.prototype.toString.call(arr) !== '[object Array]') {
  	return [];
  }
  
  let result = [];
  for(let idx = 0 ;idx < arr.length; idx++) {
  	if(callback(arr[idx])) {
    	result.push(arr[idx])
    }
  }
  
  return result;
  
} 
console.log([].myFilter((elem) => elem % 2 === 0))

// reduce

Array.prototype.myReduce = function(callback, start) {
	const arr = this;
  if(!arr || typeof callback !== 'function' || Object.prototype.toString.call(arr) !== '[object Array]') {
  	return [];
  }
  
  let acc = start;
  /* let acc = start; */
  for(let idx = 0 ;idx < arr.length; idx++) {
  	acc = callback(acc, arr[idx]);
  }
  
  return acc;
  
} 

console.log([1,2,3].myReduce((acc, current) => current * acc, 1))
