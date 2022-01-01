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
      () => {
        this.state.lang === "ag" && this.setState({ lang: "en" })  // set to english when `all languages` was choosen
        console.log("set lang to: " + this.state.lang);
      });
  }

  render() {
    console.log(this.state.lang)
    return (
      <>
        <div className={this.state.lang}>
          <Head slang={this.state.lang} updateLang={this.updateLang} />
          <Search sLang={this.state.lang} />
          <footer><a href="http://t.me/RobotTrickBot">Conenct us!</a></footer>
        </div>
      </>
    );
  }
}
