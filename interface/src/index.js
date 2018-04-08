import {render} from "inferno";
import App from "./App";
import "./index.css";
import {BrowserRouter, Route} from "inferno-router";

const Page = () =>
  <BrowserRouter>
    <Route path="/:id" component={App} />
  </BrowserRouter>;

render(<Page />, document.getElementById("app"));
