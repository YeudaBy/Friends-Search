import React from "react";
import { NavBar } from "./TestNavBar"
import HomeHeadline from "./Headline"

export default function Head(props) {
    return (
        <div className="Head">
            <NavBar sLang={props.sLang} updateSLang={props.updateSLang}/>
            <HomeHeadline sLang={props.sLang} />
        </div>
    )
}