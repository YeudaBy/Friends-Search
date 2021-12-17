import { Search } from "./components/Search";
import Head from "./components/Head";
import "./App.css"
import React from "react";

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { lang: "en" }

    this.updateLang = this.updateLang.bind(this);
  }

  updateLang(event) {
    this.setState({ lang: event.nativeEvent.target.value },
      () => { console.log("set lang to: " + this.state.lang); });
  }

  render() {
    return (
      <>
        <Head lang={this.state.lang} updateLang={this.updateLang} />
        <Search lang={this.state.lang} />
      </>
    );
  }
}
