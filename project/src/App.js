import React, {Component} from 'react';
//import logo from './logo.svg';
import './App.css'; 
import Side from './components/SideLayout';

import 'rsuite/dist/styles/rsuite-default.css';
//import { Button } from 'rsuite';  
import { Container, Header, Content, Footer, Sidebar } from 'rsuite';

class App extends Component{ 
    render(){
        return( 
            <Side /> 

        );

    }
}

export default App; 
