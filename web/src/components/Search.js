import React from "react";
import ResultsList from "./ResultsList";
import SearchField from "./SearchField";
import SelectLang from "./SelectLang";

export class Search extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      results: [],
      error: null,
      lang: 'en',
      langs: []
    };

    this.searchChange = this.searchChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.langChange = this.langChange.bind(this);
    this.changeLang = this.changeLang.bind(this);

    this.baseUrl = "http://127.0.0.1:8080/"
  }

  componentDidMount() {
    fetch(this.baseUrl + "language")
      .then(res => res.json())
      .then((res) => this.setState({langs: res}))
  }

  searchChange(event) {
    this.setState({ value: event.target.value });
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

  changeLang(event) {
    this.setState({lang: event.nativeEvent.target.value})
  }

  componentDidUpdate() {
    document.title = `Friends Search - Results for ${this.state.value}`;
  }

  render() {
    return (<div className="container">
      <SearchField
        searchChange={this.searchChange}
        handleSubmit={this.handleSubmit}
        value={this.value}
      />

      <SelectLang value={this.state.lang} changeLang={this.changeLang} langs={this.state.langs} />

      <ResultsList results={this.state.results} />
    </div>
    );
  }
}