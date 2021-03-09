const MyReact = (function() {
  let _val // hold our state in module scope
  return {
    useState: (initialValue) => {
      _val = _val || initialValue // assign anew every run
      function setState(newVal) {
        _val = newVal
      }
      console.log(_val, 'test')
      return [_val, setState]
    }
  }
})()


const [value, setValue] = MyReact.useState(3)
console.log(setValue(7)) 
console.log(MyReact.useState())
console.log(value)