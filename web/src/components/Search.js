import React from "react";
import ResultsList from "./ResultsList";
import SearchField from "./SearchField";
import SelectLang from "./SelectLang";
import getStr from "../strings";

export class Search extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      results: [],
      error: null,
      lang: 'en',
      langs: [],
      dir: 'ltr',
      submited: false
    };

    this.searchChange = this.searchChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.langChange = this.langChange.bind(this);
    this.updateLang = this.updateLang.bind(this);

    this.baseUrl = "http://api.friends-search.com/"
  }

  componentDidMount() {
    fetch(this.baseUrl + "language")
      .then(res => res.json())
      .then((res) => this.setState({ langs: res }))
      .catch((error) => console.error(error),
        this.setState({
          langs: {
            "ag": "All languages",
            "en": "English",
            "fr": "Français",
            "he": "עברית"
          }
        }))
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
      ).catch((err) => this.setState({
        error: err
      }));
    this.setState({ submited: true })
    event.preventDefault();
  };

  updateLang(event) {
    this.setState({ lang: event.nativeEvent.target.value })
  }

  render() {
    return (<div className="container center">
      <div className="search">
        <SearchField
          searchChange={this.searchChange}
          handleSubmit={this.handleSubmit}
          value={this.state.value}
          sLang={this.props.sLang}
        />

        <SelectLang
          label={getStr("slng-search", this.props.sLang)}
          value={this.state.lang}
          updateLang={this.updateLang}
        />
      </div>

      {this.state.submited === true &&
        <ResultsList
          results={this.state.results}
          dir={this.state.dir}
          sLang={this.props.sLang}
        />
      }
    </div>
    );
  }
}