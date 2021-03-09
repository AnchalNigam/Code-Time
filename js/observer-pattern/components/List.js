import Observer from '../lib/observer';

class List extends Observer {
  createMarkup(state) {
    return <ul>
      {state.user.map((user) => <li>{user.name}</li>)}
    </ul>
  }
  render(state, selector ) {
    const elementId = document.getElementById(selector);
    const markup = this.createMarkup(state);
    elementId.innerHTML = markup;
  }

  update(state) {
    this.render(state, selector);
  }
}

export default List;