function getFlattenArray() {
  var newArray = [];
	function flattenArray(arr, res) {
  for(let idx = 0; idx < arr.length; idx++) {
    if(Array.isArray(arr[idx])) {
      flattenArray(arr[idx], res)
    } else {
      res.push(arr[idx])
    }
  }
} 
  flattenArray(arr, newArray)
  return newArray;
}