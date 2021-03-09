import Subject from './subject';

class State extends Subject {
  constructor() {
    super()
      this.state = {};
  }

  get() {
    return this.state;
  }

  update(data = {}) {
    this.state = Object.assign(this.state, data);
    this.notify(this.state);
  }
}


export default State;