import 'rsuite/dist/styles/rsuite-default.css';
//import { Button } from 'rsuite';  
import { Container, Header, Content, Footer, Sidebar, Navbar, Nav, Sidenav, Icon, Dropdown } from 'rsuite';   
import React, {Component} from 'react'; 
//import { Button, Navbar, Nav, Sidenav, Icon, Dropdown, } from 'react-bootstrap'

import {Link, Router} from 'react-router-dom';  
import Dairy from './Dairy'; 
import ReactDOM from 'react-dom'


const headerStyles = {
  padding: 18,
  fontSize: 16,
  height: 56,
  background: '#34c3ff',
  color: ' #fff',
  whiteSpace: 'nowrap',
  overflow: 'hidden'
};

const iconStyles = {
  width: 56,
  height: 56,
  lineHeight: '56px',
  textAlign: 'center'
};

const NavToggle = ({ expand, onChange }) => {
  return (
    <Navbar appearance="subtle" className="nav-toggle">
      <Navbar.Body>
        <Nav>
          <Dropdown
            placement="topStart"
            trigger="click"
            renderTitle={children => {
              return <Icon style={iconStyles} icon="cog" />;
            }}
          >
            <Dropdown.Item>Help</Dropdown.Item>
            <Dropdown.Item>Settings</Dropdown.Item>
            <Dropdown.Item>Sign out</Dropdown.Item>
          </Dropdown>
        </Nav>

        <Nav pullRight>
          <Nav.Item onClick={onChange} style={{ width: 56, textAlign: 'center' }}>
            <Icon icon={expand ? 'angle-left' : 'angle-right'} />
          </Nav.Item>
        </Nav>
      </Navbar.Body>
    </Navbar>
  );
}; 

class Side extends Component { 

  constructor(props) {
    super(props);
    this.state = {
      expand: true
    };
    this.handleToggle = this.handleToggle.bind(this); 
    this.loadDairy = this.loadDairy.bind(this);
  }
  handleToggle() {
    this.setState({
      expand: !this.state.expand
    });
  } 
  loadDairy() {
    ReactDOM.render(<Dairy />, document.getElementById('root')); 
  }
  render() {
    const { expand } = this.state;
    return (
      <div className="show-fake-browser sidebar-page">
        <Container>
          <Sidebar
            style={{ display: 'flex', flexDirection: 'column' }}
            width={expand ? 260 : 56}
            collapsible
          >
            <Sidenav.Header>
              <div style={headerStyles}>
                <Icon icon="logo-analytics" size="lg" style={{ verticalAlign: 0 }} />
                <span style={{ marginLeft: 12 }}> BRAND</span>
              </div>
            </Sidenav.Header>
            <Sidenav
              expanded={expand}
              defaultOpenKeys={['3']}
              appearance="subtle"
            >
              <Sidenav.Body>
                <Nav>
                  <Nav.Item eventKey="1" active icon={<Icon icon="dashboard" />}>
                    Dashboard
                  </Nav.Item>
                  <Nav.Item eventKey="2" icon={<Icon icon="group" />}>
                    User Group
                  </Nav.Item>
                  <Dropdown
                    eventKey="3"
                    trigger="hover"
                    title="Items"
                    icon={<Icon icon="magic" />}
                    placement="rightStart"
                  > 
                    <Dropdown.Item eventKey="3-1" onclick={this.loadDairy}>Meat</Dropdown.Item>
                    <Dropdown.Item eventKey="3-2">Dairy</Dropdown.Item>
                    <Dropdown.Item eventKey="3-3">Beverages</Dropdown.Item>
                    <Dropdown.Item eventKey="3-4">Personal Care</Dropdown.Item>
                    <Dropdown.Item eventKey="3-5">Other</Dropdown.Item> 
                  </Dropdown>
                
                </Nav>
              </Sidenav.Body>
            </Sidenav>
            <NavToggle expand={expand} onChange={this.handleToggle} />
          </Sidebar>

          <Container>
            <Header>
              <h2>Page Title</h2>
            </Header>
            <Content>Content</Content>
          </Container>
        </Container>
      </div>
    );
  } 
  
}

//ReactDOM.render(<Page />); 

export default Side;