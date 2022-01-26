import { Home } from "./components/Home";
import { Game } from "./components/Game"
import { About } from "./components/About"
import Details from "./components/Details"
import Page from "./components/Page"

import "./App.css"
import React from "react";
import { browserLanguage } from "./languages"
import { BrowserRouter, Route, Routes } from "react-router-dom";



export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { sLang: browserLanguage() }

    this.updateSLang = this.updateSLang.bind(this);
  }

  updateSLang(event) {
    // console.log(event.target.value)
    this.setState({ sLang: event.target.value },
      console.log("set site language to: " + this.state.sLang));
  }

  render() {
    return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Page />} >
            <Route path="/home" element={<Home sLang={this.state.sLang} updateSLang={this.updateSLang}/>} />
            <Route path="/game" element={<Game />} />
            <Route path="/about" element={<About />} />
            <Route path="/sentence/" element={<Details />} />
          </Route>

        </Routes>
      </BrowserRouter>
    );
  }
}
