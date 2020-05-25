import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import { Container, Image, Button } from 'react-bootstrap';

class App extends Component {
  render() {
    return (
      <Container>
        <Image></Image>
        <Button>Click Here</Button>
      </Container>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('app'));
