Function.prototype.myCall = function (callObj, ...args){
  callObj.fnName = this;
  callObj.fnName(...args);
}

introToInterviewer.myCall(intervieweeObj, 'allahabd', 'artist') 

// apply code self
Function.prototype.myApply = function (applyObj, args){
  applyObj.fnName = this;
  applyObj.fnName(...args);
}

introToInterviewer.myApply(intervieweeObj, ['allahabd', 'artist']) 

Function.prototype.myBind = function (bindObj, ...args1){
  var context = this;
  return function (...args2) {
    context.myApply(bindObj, [...args1, ...args2]);
  }; 
} 
 
const bindedFunc = introToInterviewer.myBind(intervieweeObj);
bindedFunc('allahabad', 'soft')

// apply code online
if (!Function.prototype.bind) {
  Function.prototype.bind = function() {
    const thisCtx = this;
    const boundCtx = arguments[0];
    const boundArgs = Array.from(arguments).slice(1);

    if (typeof thisCtx !== 'function') {
      throw new TypeError('Not a valid function');
    }

    return function() {
      const allArguments = boundArgs.concat(Array.from(arguments));
      thisCtx.apply(boundCtx, allArguments);
    };
  };
}