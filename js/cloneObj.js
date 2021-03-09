function cloneObjectDeep(obj) {
  let target = {}
	for(const key in obj) {
  	console.log(key)
    if(Object.prototype.toString.call(obj[key]) === "[object Object]") {
       target[key] = cloneObjectDeep(obj[key])
    } else {
    	target[key] = obj[key]
    }
	}
  return target

}
