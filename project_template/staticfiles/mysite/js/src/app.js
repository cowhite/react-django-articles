import React from "react";
import { render } from "react-dom";
import {
  createStore,
  compose,
  applyMiddleware,
  combineReducers,
} from "redux";
import { Provider } from "react-redux";
import thunk from "redux-thunk";

import * as reducers from "./reducers";


import AppContainer from "./containers/AppContainer";

let finalCreateStore = compose(
  applyMiddleware(thunk),
  window.devToolsExtension ? window.devToolsExtension() : f => f
)(createStore)
let reducer = combineReducers(reducers)
let store = finalCreateStore(reducer)


class App extends React.Component{
  render(){
    return (
       <Provider store={store}>
        <AppContainer />
      </Provider>
    );
  }
}

render(<App/>, window.document.getElementById("app"));