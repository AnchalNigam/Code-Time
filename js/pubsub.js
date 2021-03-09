const pubsub = (function () {
  const subscribers = {};
  const publish = (event, data) => {
  	if(!Array.isArray(subscribers[event])) {
    	return;
    }
    
    subscribers[event].forEach((subscriberCallback) => {
    	subscriberCallback(data);
    })
  }
  
  const subscribe = (event, subscriberCallback) => {
  	if(!subscribers[event]) {
    	subscribers[event] = [];
    }
    
    index = subscribers[event].push(subscriberCallback) - 1;
    return {
    	unsubscribe: function () {
      	subscribers[event].splice(index,1);
      }
    }
    
  }
	return {
  	publish: publish,
    subscribe: subscribe,
  }
})();


const subscription = pubsub.subscribe('anchalChannel', (data) => {
	console.log(data);
})
pubsub.subscribe('anchal', (data) => {
	console.log(data);
})
subscription.unsubscribe();
pubsub.publish('anchalChannel', 'Here is my new article');
