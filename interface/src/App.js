import {Component} from "inferno";
import "./registerServiceWorker";
import "./App.css";
import io from "socket.io-client";
import moment from "moment";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      geolocation: {},
      orientation: {}
    };
    console.log(props)
    this.getSensors = this.getSensors.bind(this);
    this.socket = io("/phones");
    this.socket.on("identify", (fn) => fn(props.match.params.id));
    this.getSensors();
  }
  getSensors() {
    let self = this;

    if (navigator.geolocation) {
      navigator.geolocation.watchPosition(
        position => {
          let {coords = {}, timestamp = 0} = position;
          let geolocation = {coords, timestamp};
          let {latitude, longitude, altitude} = coords;
          self.setState({geolocation});
          this.socket.emit("geolocation", {
            latitude,
            longitude,
            altitude,
            timestamp
          });
        },
        error => {
          self.setState({geolocation: error});
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
        "deviceorientation",
        data => {
          let {alpha, beta, gamma} = data;
          let orientation = {alpha, beta, gamma};

          self.setState({orientation});
          self.socket.emit("orientation", orientation);
        },
        false
      );
    }
  }
  render() {
    let {geolocation = {}, orientation = {}} = this.state;
    let {coords = {}, timestamp = 0} = geolocation;
    let {alpha = 0, beta = 0, gamma = 0} = orientation;
    return (
      <div className="App">
        <div>
          <h3>Geolocation</h3>
          <code>
            Latitude {coords.latitude}
            <br />
            Longitude {coords.longitude}
            <br />
            Altitude {coords.altitude}
            <br />
            Time {moment(timestamp).format()}
            <br />
          </code>
        </div>
        <div>
          <h3>Orientation</h3>
          <code>
            Alpha {alpha.toFixed(2)}
            <br />
            Beta {beta.toFixed(2)}
            <br />
            Gamma {gamma.toFixed(2)}
            <br />
          </code>
        </div>
      </div>
    );
  }
}

export default App;
