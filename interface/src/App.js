import {Component} from 'inferno';
import './registerServiceWorker';
import './App.css';
import io from 'socket.io-client';
import moment from 'moment';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      geolocation: {},
      orientation: {}
    };

    this.getSensors = this.getSensors.bind(this);
    this.getPicture = this.getPicture.bind(this);
    this.startCamera = this.startCamera.bind(this);
    this.socket = io('/phones');
    this.socket.on('identify', fn => fn(props.match.params.id));
    this.socket.on('get_picture', this.getPicture);
  }
  componentDidMount() {
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
          this.socket.emit('geolocation', {
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
        'deviceorientation',
        data => {
          let {alpha, beta, gamma} = data;
          let orientation = {alpha, beta, gamma};

          self.setState({orientation});
          self.socket.emit('orientation', orientation);
        },
        false
      );
    }
  }
  getPicture(callback) {
    let context = this.canvas.getContext('2d');
    this.canvas.width = this.width;
    this.canvas.height = this.height;
    context.drawImage(this.video, 0, 0, this.width, this.height);
    let data = this.canvas.toDataURL('image/jpeg');
    callback(data);
  }
  async startCamera() {
    this.video = document.getElementById('video');
    this.canvas = document.getElementById('canvas');
    this.width = 640;
    this.video.srcObject = await navigator.mediaDevices.getUserMedia({
      video: true,
      audio: false
    });
    this.video.addEventListener(
      'canplay',
      ev => {
        this.height =
          this.video.videoHeight / (this.video.videoWidth / this.width);
        this.video.setAttribute('width', this.width);
        this.video.setAttribute('height', this.height);
        this.canvas.setAttribute('width', this.width);
        this.canvas.setAttribute('height', this.height);
      },
      false
    );

    this.video.play();
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
        {/*
        <div className="camera">
          <button type="button" onClick={this.startCamera}>
            Iniciar Camara
          </button>
          <video id="video">Camera not available</video>
        </div>
        <canvas id="canvas" />*/}
      </div>
    );
  }
}

export default App;
