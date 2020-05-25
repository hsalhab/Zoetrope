import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import { Container, Image, Button, Row, Col } from 'react-bootstrap';

import '../styles/main.scss';

class App extends Component {
  render() {
    return (
      <Container>
        <br/><br/><br/>
        {/* TODO: center vertically */}
        <Row>
          <Col className='text-center'>
            <Image src=""></Image>
          </Col>
        </Row>
        <br/>
        <Row>
          <Col className='text-center'>
            <Button>Click Here</Button>
          </Col>
        </Row>
      </Container>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
