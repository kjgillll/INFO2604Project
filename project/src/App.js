import React from 'react';
//import logo from './logo.svg';
import './App.css';

import 'rsuite/dist/styles/rsuite-default.css';
import { Button } from 'rsuite'; 

function App() {
  return (
    <div className="App">
      <Button appearance="primary"> Hello world </Button> 
      <p>My Token = {window.token}</p>
    </div>
  );
}

export default App; 
