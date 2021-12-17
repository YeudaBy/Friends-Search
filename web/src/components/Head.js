import React from "react";
import SelectLang from "./SelectLang";
import HeadNav from "./HeadNav"

export default function Head(props) {

    function changeLange(e) {
        props.updateLang(
            e.nativeEvent.target.value
        )
    }

    return(
        <>  
            <HeadNav />
            <SelectLang label={"Select site lang"} changeLang={props.changeLange()}/>
            <h1>Friends Search</h1>
        </>
    )
}