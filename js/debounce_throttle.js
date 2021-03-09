const debounce = (func, delay) => {
	clearTimeout(timerId)
  timerId = setTimeout(func, delay)
}

const throttle = (func, delay) => {
	if(timerId) {
  	return
  }
  timerId = setTimeout(function() {
  	func()
    timerId = undefined
    }, delay)
}

function abc() {
  console.log('test');
 }
 let debounce = (function (func, delay) {
   let timerId;
   return function(...args) {
     console.log(func, 'check')
     clearTimeout(timerId);
     timerId = setTimeout(func, delay);
   }
 
 })(abc, 1000);
 
 /* const debounced = debounce(abc, 1000) */
 document.addEventListener("keyup", debounce);
 
 /* document.addEventListener('keyup', () => console.log('hi')) */

// react

// https://dev.to/gabe_ragland/debouncing-with-react-hooks-jci