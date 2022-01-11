import React from "react";
import ResultsList from "./ResultsList";
import SearchField from "./SearchField";
import SelectLang from "./SelectLang";
import { browserLanguage } from "../languages"
import { Error, Loading, NoResults } from "./StatusSearch"


let baseUrl = "https://api.friends-search.com/"
baseUrl = "http://192.168.43.122:8080/"

export class Search extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      searchValue: '',
      searchResult: {
        results: [],
        count: 0,
        error: null,
        isLoaded: false
      },
      searchLang: browserLanguage() !== "en" ? browserLanguage() : "ag",
      submited: false,
    };

    this.searchChange = this.searchChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.updateSearchLang = this.updateSearchLang.bind(this);
  }


  searchChange(event) {
    this.setState({ searchValue: event.target.value });
  };

  updateSearchLang(event) {
    this.setState({ searchLang: event.nativeEvent.target.value })
  }

  handleSubmit(event) {
    const endpoint = baseUrl + "sentence/search"
    const url = `${endpoint}?query=${this.state.searchValue}&language=${this.state.searchLang}&limit=50`
    if (typeof this.state.searchValue !== "undefined" & this.state.searchValue !== "") {
      this.setState({ submited: true })
      fetch(url)
        .then(res => res.json())
        .then(
          (results) => {
            this.setState({
              searchResult: {
                results: results.results,
                count: results.count,
                isLoaded: true,
                error: results.error
              }
            }, console.log("results from the server: ", this.state.searchResult));
          },
          (error) => {
            this.setState(preState => ({
              searchResult: {
                ...preState.searchResult,
                isLoaded: true,
                error: error
              }
            }), console.error(this.state.searchResult.error));
          }
        ).catch(
          (error) => {
            this.setState(preState => ({
              searchResult: {
                ...preState.searchResult,
                isLoaded: true,
                error: error
              }
            }), console.error(this.state.searchResult.error));
          });
    };
    event.preventDefault();
  };

  render() {
    return (
      <div className="container center">
        <div className="search">
          <SearchField
            searchChange={this.searchChange}
            handleSubmit={this.handleSubmit}
            value={this.state.value}
            sLang={this.props.sLang}
          />

          <SelectLang updateSearchLang={this.updateSearchLang} value={this.state.searchLang} />
        </div>

        <div className="resultsView">

          {
            (this.state.submited === false)
              ? <>{""}</>
              : (this.state.submited === true & this.state.searchResult.isLoaded === false)
                ? <Loading sLang={this.props.sLang} />
                : (this.state.searchResult.isLoaded === true & (typeof this.state.searchResult.error !== "undefined"
                  & this.state.searchResult.error !== null))
                  ? <Error sLang={this.props.sLang} />
                  : (this.state.searchResult.isLoaded === true & (typeof this.state.searchResult.error === "undefined"
                    | this.state.searchResult.error === null) & (this.state.searchResult.count === 0
                      | typeof this.state.searchResult.results === "undefined"))
                    ? <NoResults sLang={this.props.sLang} />
                    : <ResultsList count={this.state.searchResult.count}
                      results={this.state.searchResult.results} sLang={this.props.sLang} />
          }

        </div>
      </div>
    );
  }
}