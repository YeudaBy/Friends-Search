import React from "react";

const baseUrl = "http://127.0.0.1:8080/"

export default class SelectLang extends React.Component {
    constructor(props) {
        super(props)
        this.state = {langs: {}}
        this.loadLangs = this.loadLangs.bind(this);
    }

    loadLangs(e){
        fetch(baseUrl + "language")
            .then((res) => res.json())
            .then((res) => this.setState({langs: res}));
    }
    
    render() {
        const langs = this.state.langs;
        return (
            <details>
                <summary onClick={this.loadLangs}>{this.props.label}</summary>
                <div className="selectLang">
                <select value={this.props.value} onChange={this.props.changeLang}>

                {Object.keys(langs).length > 0 && Object.keys(langs).map((key) => {
                    return <option key={key} value={key} >{langs[key]}</option>
                })}

                </select>

            </div>
            </details>
        )
    }
}