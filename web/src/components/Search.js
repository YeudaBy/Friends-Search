import React from "react";
import ResultsList from "./ResultsList";
import SearchField from "./SearchField";
import SelectLang from "./SelectLang";
import getStr from "../strings";
import { Error, Loading, NoResults } from "./StatusSearch"

export class Search extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: '',
      results: {
        resultsList: [],
        count: 0
      },
      error: null,
      lang: 'en',
      langs: [],
      dir: 'ltr',
      submited: false,
      isLoaded: false
    };

    this.searchChange = this.searchChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.langChange = this.langChange.bind(this);
    this.updateLang = this.updateLang.bind(this);

    this.baseUrl = "https://api.friends-search.com/"
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
    this.setState({ value: event.target.value });
  }

  langChange(event) {
    this.setState({ lang: event.target.value })
  }

  handleSubmit(event) {
    const url = this.baseUrl + "sentence/search"
    if (typeof this.state.value !== "undefined" & this.state.value !== "") {
      fetch(`${url}?query=${this.state.value}&language=${this.state.lang}&limit=50`)
        .then(res => res.json())
        .then(
          (result) => {
            this.setState(preState => ({
              results: {
                ...preState.results,
                resultsList: result.results,
                count: result.count,
              },
              isLoaded: true,
            }), console.log("results from the server: ", this.state.results),
            );
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        ).catch(
          (error) => {
            this.setState({
              error
            })
          });
      this.setState({ submited: true })
    };
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

      {
        this.state.submited === false ?
          <>{""}</> :
          this.state.isLoaded === false & this.state.submited === true ?
            <Loading /> :
            this.state.isLoaded === true && this.state.results.count === 0 ?
              <NoResults /> :
              this.state.error !== null ?
                <Error error={this.state.error} /> :
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