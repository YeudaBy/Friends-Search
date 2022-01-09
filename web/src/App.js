import { Search } from "./components/Search";
import Head from "./components/Head";
import "./App.css"
import React from "react";
import { GoMention } from "react-icons/go"

// function getBrowserLang() {
//   let Browslanguage = window.navigator.userLanguage || window.navigator.language
//   return /^([a-z]*)/.exec(Browslanguage)[0]
// }

export default class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { lang: "en" }

    this.updateLang = this.updateLang.bind(this);
  }

  updateLang(event) {
    console.log(event.target.dataset)
    this.setState({ lang: event.target.dataset.key },
      () => {
        this.state.lang === "ag" && this.setState({ lang: "en" })  // set to english when `all languages` was choosen
        console.log("set lang to: " + this.state.lang);
      });
  }

  render() {
    return (
      <>
        <div className={this.state.lang}>
          <Head slang={this.state.lang} updateLang={this.updateLang} />
          <Search sLang={this.state.lang} />
        </div>
      </>
    );
  }
}
