const user = {
	name: 'anchal',
  address: {
    street: 12,
    town: 'allahabad',
    state: 'up',
    office: {
    	landmark: 'near palace'
    }
  }
}

/* op 
user.name = 'anhcal',
user.address.street = 12
user.address.town = allahabad
user.address.state = up
user.address.office.landmark = near palace

*/

function flattenObj() {
  const finalObj = {};
	function flat(obj, parentName) {
    for(const key in obj) {
      console.log(typeof obj[key])
    	if(typeof obj[key] === 'object') {
       /*  console.log(obj[key], 'test') */
      	flat(obj[key], parentName + '.' + key)
    	} else {
        finalObj[parentName + '.' + key] = obj[key]
      }
      
    }
  
  }
  flat(user, 'user')
  return finalObj
}