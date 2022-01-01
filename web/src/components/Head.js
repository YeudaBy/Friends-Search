import React from "react";
import HeadNav from "./HeadNav"

export default function Head(props) {
    return (
        <div className="Head">
            <HeadNav updateLang={props.updateLang} sLang={props.sLang}/>
            <h1 className="center">Friends Search</h1>
        </div>
    )
}