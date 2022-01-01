import React from "react";

const baseUrl = "http://127.0.0.1:8080/"

export default class SelectLang extends React.Component {
    constructor(props) {
        super(props)

        this.state = { langs: {} }
        this.loadLangs = this.loadLangs.bind(this);
    }

    loadLangs(e) {
        // fetch languages list
        fetch(baseUrl + "language")
            .then((res) => res.json())
            .then((res) => this.setState({ langs: res }))
            .catch((error) => console.error(error),
                this.setState({
                    langs: {
                        "ag": "All languages",
                        "en": "English",
                        "fr": "Français",
                        "he": "עברית"
                    }
                }));
    }

    render() {
        const langs = this.state.langs;
        return (
            <details>
                <summary onClick={this.loadLangs}>{this.props.label}</summary>  { /* label for language selector */}

                <div className="selectLang">
                    <select value={this.props.sLang} onChange={this.props.updateLang}>

                        {Object.keys(langs).length > 0 && Object.keys(langs).map((key) => {
                            return <option key={key} value={key} >{langs[key]}</option>
                        })}  { /* all the languages */}

                    </select>
                </div>

            </details>
        )
    }
}