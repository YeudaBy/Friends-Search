import React from "react";
import HeadNav from "./HeadNav"

export default function Head(props) {
    return (
        <div className="Head">
            <HeadNav updateLang={props.updateLang} sLang={props.sLang}/>
            <h1 className="center notranslate">F<span className="red">•</span>r<span className="blue">•</span>
            i<span className="yelow">•</span>e<span className="red">•</span>n
            <span className="yelow">•</span>d<span className="blue">•</span>s Search</h1>
        </div>
    )
}