import React from "react";
import ResultsList from "./ResultsList";
import SearchField from "./SearchField";
import SelectLang from "./SelectLang";
// import getStr from "../strings"

export class Search extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      results: [],
      error: null,
      lang: 'en',
      langs: [],
      dir: 'ltr'
    };

    this.searchChange = this.searchChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.langChange = this.langChange.bind(this);
    this.updateLang = this.updateLang.bind(this);

    this.baseUrl = "http://127.0.0.1:8080/"
  }

  componentDidMount() {
    fetch(this.baseUrl + "language")
      .then(res => res.json())
      .then((res) => this.setState({ langs: res }))
  }

  searchChange(event) {
    this.setState({ value: event.target.value },
      () => {
        if (this.state.lang === "he") this.setState({ dir: "rtl" })
      });
  }

  langChange(event) {
    this.setState({ lang: event.target.value })
  }

  handleSubmit(event) {
    const url = this.baseUrl + "sentence/search"
    fetch(`${url}?query=${this.state.value}&language=${this.state.lang}`)
      .then(res => res.json())
      .then(
        (result) => { this.setState({ results: result.results }); },
        (error) => { this.setState({ error }); }
      );
    event.preventDefault();
  };

  updateLang(event) {
    this.setState({ lang: event.nativeEvent.target.value })
  }

  componentDidUpdate() {
    document.title = `Friends Search - Results for ${this.state.value}`;
  }

  render() 
  {
    return (<div className="container center">
      <div className="search">
        <SearchField
          searchChange={this.searchChange}
          handleSubmit={this.handleSubmit}
          value={this.state.value}
        />

        <SelectLang
          label={"Select Languege To Search"}
          value={this.state.lang}
          updateLang={this.updateLang}
        />
      </div>

      <ResultsList results={this.state.results} dir={this.state.dir} />
    </div>
    );
  }
}