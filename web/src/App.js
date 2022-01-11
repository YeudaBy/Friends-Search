import { Search } from "./components/Search";
import Head from "./components/Head";
import "./App.css"
import React from "react";
import { browserLanguage } from "./languages"

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
      <>
        <div className={this.state.sLang}>
          <Head sLang={this.state.sLang} updateSLang={this.updateSLang} />
          <Search sLang={this.state.sLang} />
        </div>
      </>
    );
  }
}
