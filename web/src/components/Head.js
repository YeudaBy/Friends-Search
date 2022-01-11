import React from "react";
import { NavBar } from "./TestNavBar"

export default function Head(props) {
    return (
        <div className="Head">
            <NavBar sLang={props.sLang} updateSLang={props.updateSLang}/>
            <h1 className="center notranslate">F<span className="red">•</span>r<span className="blue">•</span>
            i<span className="yelow">•</span>e<span className="red">•</span>n
            <span className="yelow">•</span>d<span className="blue">•</span>s Search</h1>
        </div>
    )
}