arr = [100, 34, 45, 2]
function mergeArr(L, R) {
const result = []
console.log(L, R, 'pp')
	var i = j = k = 0;
  while(i < L.length && j < R.length) {
  	if(L[i] < R[j]) {
    	result.push(L[i])
      i += 1
    } else {
      result.push(R[j])
     j += 1
    }
    k += 1
  }
  while(i < L.length) {
  	result.push(L[i])
    k += 1
    i += 1
  }
  while(j < R.length) {
  	 result.push(R[j])
    j += 1
    k += 1
  }
  console.log(result, 'res')
  return result
}
function mergeSort(arr) {
if(arr.length <= 1) return arr
	    let mid = parseInt(arr.length/2)
	    let L = mergeSort(arr.slice(0,mid))
	    let R = mergeSort( arr.slice(mid))
	    return mergeArr(L,R)

}

console.log(mergeSort(arr), 'check')
