import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import { UserList } from './components/users';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to React</h2>
        </div>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <UserList />
      </div>
    );
  }
}

export default App;


// // in src/App.tsx
// import { Admin } from "react-admin";
// import jsonServerProvider from "ra-data-json-server";

// const dataProvider = jsonServerProvider('https://jsonplaceholder.typicode.com');

// const App = () => <Admin dataProvider={dataProvider} />;

// export default App;