import React from "react";
import { NextBtn, PreviousBtn } from "./NavigBtn"
import getStr from "../strings"

const baseUrl = "http://api.friends-search.com/"

export class Result extends React.Component {
    constructor(props) {
        super(props);
        this.state = { ...props }

        this.NextBtnHandler = this.NextBtnHandler.bind(this);
        this.PreviousBtnHandler = this.PreviousBtnHandler.bind(this);
    }

    NextBtnHandler() {
        fetch(baseUrl + "sentence/" + (this.state.id + 1))
            .then((res) => res.json())
            .then((res) => this.setState(res));
    }

    PreviousBtnHandler() {
        fetch(baseUrl + "sentence/" + (this.state.id - 1))
            .then((res) => res.json())
            .then((res) => this.setState(res));
    }

    render() {
        return (
            <details className="result">
                <summary
                    className="resultSum"
                >
                    {this.state.content}
                </summary>

                <div className="resultInDiv">

                    <p>
                        {getStr("season", this.props.sLang) + " "}
                        {this.state.season}
                        {" • "}
                        {getStr("episode", this.props.sLang) + " "}
                        {this.state.episode} 
                        <br />
                        {/(\d:)(\d{2}:\d{2})(.\d*)/.exec(this.state.start)[2]}
                        {" "} &#x21FF; {" "}
                        {/(\d:)(\d{2}:\d{2})(.\d*)/.exec(this.state.end)[2]}
                    </p>

                    <PreviousBtn handle={this.PreviousBtnHandler} sLang={this.props.sLang}/>

                    <NextBtn handle={this.NextBtnHandler} sLang={this.props.sLang}/>

                    {/* <Details res={this.state}/> */}



                </div>

            </details>
        )
    }
}
