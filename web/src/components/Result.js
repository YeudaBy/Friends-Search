import React from "react";
import { NextBtn, PreviousBtn } from "./NavigBtn"
import Details from "./PopUp"

const baseUrl = "http://127.0.0.1:8080/"

export class Result extends React.Component {
    constructor(props) {
        super(props);
        this.state = { ...props }

        this.NextBtnHandler = this.NextBtnHandler.bind(this);
        this.PreviousBtnHandler = this.PreviousBtnHandler.bind(this);
        // this.isOpen = this.isOpen.bind(this);
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

                    <p>Season {this.state.season} x Episode {this.state.episode
                    } x {/(\d:)(\d{2}:\d{2})(.\d*)/.exec(this.state.start)[2]} - {
                            /(\d:)(\d{2}:\d{2})(.\d*)/.exec(this.state.end)[2]}</p>


                    <NextBtn handle={this.NextBtnHandler} />

                    {/* <Details res={this.state}/> */}

                    <PreviousBtn handle={this.PreviousBtnHandler} />


                </div>

            </details>
        )
    }
}
