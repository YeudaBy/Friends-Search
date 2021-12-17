import React from "react";

export default function LinkBtn(props) {
    return (
        <a
            className="linkBtn"
            href={props.url}
            target={"_blank"}
            rel="noreferrer"
            >
                {props.label}
        </a>
    )
}