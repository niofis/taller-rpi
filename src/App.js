import {Component} from 'inferno';
import './registerServiceWorker';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
    this.getSensors = this.getSensors.bind(this);
    this.getSensors();
  }
  getSensors() {
    let self = this;

    if (navigator.geolocation) {
      navigator.geolocation.watchPosition(
        position => {
          self.setState({geolocation: position.coords.latitude + "," + position.coords.longitude});
        },
        error => {
          self.setState({geolocation: error.code});
        },
        {
          enableHighAccuracy: true,
          timeout: 5000,
          maximumAge: 0
        }
      );
    }

    if (window.DeviceOrientationEvent) {
      window.addEventListener(
        'deviceorientation',
        data => {
          let { gamma, beta, alpha } = data;
          let orientation = JSON.stringify({ gamma, beta, alpha });
          self.setState({ orientation });
        },
        false
      );
    }

    if (window.DeviceMotionEvent) {
      window.addEventListener('devicemotion', data => {
        let { acceleration: a, accelerationIncludingGravity: g, rotationRate:r } = data;
        let motion = `${a.x} ${a.y} ${a.z} ${g.x} ${g.y} ${g.z} ${r.gamma} ${r.beta} ${r.alpha}`;
        self.setState({motion});
      });
    }

    if ('ondevicelight' in window) {
      window.addEventListener('devicelight', event => {
        self.setState({devicelight: event.value + " lux"});
      });
    }

    if ('onlightlevel' in window) {
      window.addEventListener('lightlevel', event => {
        self.setState({lightlevel: event.value});
      });
    }

    if ('ondeviceproximity' in window) {
      window.addEventListener('deviceproximity', event => {
        self.setState({deviceproximity: event.value + " cm"});
      });
      window.addEventListener('userproximity', event => {
        self.setState({userproximity: event.near});
      });
    }
  }
  render() {
    let {
      geolocation,
      orientation,
      motion,
      devicelight,
      lightlevel,
      deviceproximity,
      userproximity
    } = this.state;
    return (
      <div className="App">
        <div>
          <h3>Geolocation</h3>
          {geolocation}
        </div>
        <div>
          <h3>Orientation</h3>
          {orientation}
        </div>
        <div>
          <h3>Motion</h3>
          {motion}
        </div>
        <div>
          <h3>Device Light</h3>
          {devicelight}
        </div>
        <div>
          <h3>Light Level</h3>
          {lightlevel}
        </div>
        <div>
          <h3>Device Proximity</h3>
          {deviceproximity}
        </div>
        <div>
          <h3>User Proximity</h3>
          {userproximity}
        </div>
      </div>
    );
  }
}

export default App;
