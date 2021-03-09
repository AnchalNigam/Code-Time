function interviewerGreeting(intervieweName) {
  return new Promise((resolve, reject) => {
    if(intervieweName === 'anchal') {
       resolve('yes! he is the one')
     } 
     reject('oops! someone else but, still happy')
  })
 }
 
 interviewerGreeting('anchal')
 .then((res) => console.log(res))
 .catch((err) => console.log(err))
 .finally(() => console.log('done promise'))


 // A simple promise that resolves after a given time
const timeOut = (t) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if(t === 2000) {
        reject('reject')
      }
      resolve(`Completed in ${t}`)
    }, t)
  })
}

// Resolving a normal promise.
timeOut(1000)
 .then(result => console.log(result)) // Completed in 1000

// Promise.all
Promise.all([timeOut(1000), timeOut(2000)])
 .then(result => console.log(result)) // ["Completed in 1000", "Completed in 2000"]


 const users = ['sindresorhus', 'Anchal-Nigam', 'yyx990803']

const fetchGithubProfile = async (user) => {
	try {
  	const response = await fetch(`https://api.github.com/users/${user}`);
    if(response.status === 200) {
      const jsonResponse = await response.json();
    	return {
        name: jsonResponse.name
      }
    } else {
    	throw new Error("Whoops!");
    }
   
  } catch(error) {
  	 throw new Error("Whooops ye kya");
  }
}
/* const fetchGithubProfile = (user) => {
  console.log(user, 'test')
  return new Promise((resolve, reject) => {
    fetch(`https://api.github.com/users/${user}`)
    .then((response) => response.json())
    .then((response) => {
      resolve({
        name: response.name
      })
    })
    .catch((e) => console.log(e, 'errr'))
  })
} */
const getAllUsersGithubInfo = async (users) => {
	const apiRequests = users.map((user) => {
  	return fetchGithubProfile(user)
    .then((singlePromiseRes) => singlePromiseRes)
    .catch((error) => console.log(error, user)) 
  })
  return Promise.all(apiRequests)
}

getAllUsersGithubInfo(users)
.then((allUsers) => console.log(allUsers))
.catch((error) => console.log(error))





// implementation of promise
 // implementation of promise
 class Promise {

  constructor(callingFunc) {
    this.state = "pending";
    this.value = undefined;
    this.promiseChain = [];
    this.handleError = () => {};
    this.error = "";
   /*  console.log(callingFunc, 'thanks') */
    this.resolve = this.resolve.bind(this);
    this.reject = this.reject.bind(this);
    callingFunc(this.resolve, this.reject);
  }
  
  resolve(response) {
  	/* console.log('response') */
    this.value = response;
    this.promiseChain.forEach((thenFunc) => {
      this.value = thenFunc(this.value)
    })
    this.state = "resolved";
  }
  
 reject(error) {
 /*  console.log('error') */
  
   if(this.state !== 'resolved') {
       this.state = "rejected";
       this.value = error;
       if(this.handleError) {
         this.handleError(this.value)  
       }
      /*  */
    }
  } 
  
  then(callback) {
  /* 	console.log(this.state, 'state') */
  	if(this.state === "resolved") {
    	this.value = callback(this.value)
    } else {
    	this.promiseChain.push(callback);
    }
    
    return this
  /*  console.log(callback, this.value, 'check')
   this.value = callback(this.value) 
    return this */
  }
  
 catch(callback) {
    if(!this.handleError() && this.state === "pending") {
      this.handleError = callback; 
    
    } else {
      callback(this.value)
    }
/*    
    if(this.state != "resolved") {
      this.error = callback(this.error)
      this.value = undefined
    } */
    return this
  } 
  
} 
 
function interviewerGreeting(intervieweName) {
  return new Promise((resolve, reject) => {
    if(intervieweName === 'anchal') {
     setTimeout((res) => {  
         resolve('hey!he is the one')
      }, 1000) 
     } 
      setTimeout(() => {
      	reject('oops! someone else but, still happy'); 
      }, 1000)
    
    
  })
 }
 
 interviewerGreeting('nigam')
 .then((res) => {
   console.log(res, 'ii')
  return 'anchal'
 })
 .then((res) => { 
 console.log('nigam'); 
 return res 
 })
 .catch((err) => console.log(err))
 .then((res) => console.log(res)) 




//  promse all implementation

Promise.all = (arr) => {

  let promiseRes = [];
  let resolved = 0;
  return new Promise((resolve, reject) => {
  for(let promise of arr) {
    console.log(promise, 'promise')
    flag = false;
    promise
    .then((res) => { 
    promiseRes.push(res); 
    resolved++; 
    if(resolved === arr.length) { 
      resolve(promiseRes)
     }
    })
    .catch((err) => { 
       promiseRes = []; 
       promiseRes.push(err); 
       reject(promiseRes)
     })
  }
  })
}

Promise.all = async (promises) => {
	let resolved = []
  for(const promise of promises) {
    console.log(await promise)
  	resolved.push(await promise);
  }
  return resolved;
}
Promise.all([timeOut(1000), timeOut(2000)])
 .then(result => console.log(result)) // ["Completed in 1000", "Completed in 2000"]
 .catch((err) => console.log(err))

 