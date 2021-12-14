import React from "react";
import SelectLang from "./SelectLang";

export default function Head(props) {
    return(
        <>
            <SelectLang label={"Select site lang"}/>
            <h1>Friends Search</h1>
        </>
    )
}