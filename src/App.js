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
          self.setState({geolocation: JSON.stringify(position)});
        },
        error => {
          self.setState({geolocation: JSON.stringify(error)});
        },
        {
          enableHighAccuracy: false,
          timeout: 5000,
          maximumAge: 0
        }
      );
    }

    if (window.DeviceOrientationEvent) {
      window.addEventListener(
        'deviceorientation',
        eventData => {
          self.setState({orientation: JSON.stringify(eventData)});
        },
        false
      );
    }

    if (window.DeviceMotionEvent) {
      window.addEventListener('devicemotion', data => {
        self.setState({motion: JSON.stringify(data)});
      });
    }

    if ('ondevicelight' in window) {
      window.addEventListener('devicelight', event => {
        self.setState({devicelight: JSON.stringify(event)});
      });
    }

    if ('onlightlevel' in window) {
      window.addEventListener('lightlevel', event => {
        self.setState({lightlevel: JSON.stringify(event)});
      });
    }

    if ('ondeviceproximity' in window) {
      window.addEventListener('deviceproximity', event => {
        self.setState({deviceproximity: JSON.stringify(event)});
      });
      window.addEventListener('userproximity', event => {
        self.setState({userproximity: JSON.stringify(event)});
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
          <textarea value={geolocation} rows="3" />
        </div>
        <div>
          <h3>Orientation</h3>
          <textarea value={orientation} rows="3" />
        </div>
        <div>
          <h3>Motion</h3>
          <textarea value={motion} rows="3" />
        </div>
        <div>
          <h3>Device Light</h3>
          <textarea value={devicelight} rows="3" />
        </div>
        <div>
          <h3>Light Level</h3>
          <textarea value={lightlevel} rows="3" />
        </div>
        <div>
          <h3>Device Proximity</h3>
          <textarea value={deviceproximity} rows="3" />
        </div>
        <div>
          <h3>User Proximity</h3>
          <textarea value={userproximity} rows="3" />
        </div>
      </div>
    );
  }
}

export default App;
