import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import { Container, Image, Button, Row, Col } from 'react-bootstrap';

import '../styles/main.scss';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      poster: null, 
      title: null
    };
    this.getMovie();
  }

  getMovie() {
    fetch('/api/get-movie/').then(res => res.json()).then(res => {
        this.setState({
          title: res.title,
          poster: res.poster
        });
    })
  }

  render() {
    return (
      <Container>
        <br/><br/><br/>
        {/* TODO: center vertically */}
        <Row>
          <Col className='text-center'>
            <Image src={this.state.poster}></Image>
          </Col>
        </Row>
        <br/>
        <Row>
          <Col className='text-center'>
            <h4>{this.state.title}</h4>
          </Col>
        </Row>
        <br/>
        <Row>
          <Col className='text-center'>
            <Button onClick={() => this.getMovie()}>Click Here</Button>
          </Col>
        </Row>
      </Container>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
