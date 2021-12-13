import React from "react";

const baseUrl = "http://127.0.0.1:8080/"

export default class SelectLang extends React.Component {
    constructor(props) {
        super(props)
        this.state = {langs: []}
        this.loadLangs = this.loadLangs.bind(this);
    }

    loadLangs(e){
        fetch(baseUrl + "language")
            .then((res) => res.json())
            .then((res) => this.setState({langs: res}));
    }
    
    render() {
        return (
            <details>
                <summary onClick={this.loadLangs}>Select Languege</summary>
                <div className="selectLang">
                <select value={this.props.value} onChange={this.props.changeLang}>
                {this.state.langs.map((element, index) => {
                    return <option key={index}>{element}</option>
                })}
                </select>
            </div>
            </details>
        )
    }
}