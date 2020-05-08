import React from 'react';
//import logo from './logo.svg';
import './App.css';

import 'rsuite/dist/styles/rsuite-default.css';
//import { Button } from 'rsuite';  
import { Container, Header, Content, Footer, Sidebar } from 'rsuite';

function App() {
  return (
    <div className="App">
        const instance = (
            <div className="show-container"></div> 
            <Container>
                <Header>Header</Header>
                <Container>
                    <Sidebar>Sidebar</Sidebar>
                    <Content>Content</Content>
                </Container>
                <Footer>Footer</Footer>
            </Container> 
        );
        ReactDOM.render(instance);
    </div>
  );
}

export default App; 
