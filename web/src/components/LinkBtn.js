import React from "react";

export default function LinkBtn(props) {
    return (
        <a
            className="linkBtn"
            href={props.url}>
                {props.label}
        </a>
    )
}