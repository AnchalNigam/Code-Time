const List = require('./components/List');
const State = require('./lib/state');
const users = require('./constants');


const AppState = new State();

AppState.update({ users });


List.render(AppState.get(), 'user-list-container');



