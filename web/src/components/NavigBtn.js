import React from "react";
import ReactTooltip from 'react-tooltip';
import getStr from "../strings"

export function NextBtn(props) {
    return (
        <>
            <img
                className="navBtn"
                src="./nextBtn.png"
                onClick={props.handle}
                alt="next btn"
                data-tip={getStr("n-tip", "he")}
            />
            <ReactTooltip place="right" type="dark" effect="solid" />
        </>
    )
}

export function PreviousBtn(props) {
    return (
            <>
            <img
                className="navBtn"
                src="./previousBtn.png"
                onClick={props.handle}
                alt="previous btn"
                data-tip="Previous sentence"
                data-for="previous"
            />
            <ReactTooltip id="previous" place="left" type="dark" effect="solid" />
            </>
    )
}

export function OpenBtn(props) {
    return (
        <>
        <img
            className="openBtn"
            src="./openBtn.png"
            alt="open btn"
            data-tip="Open sentence details"
            data-for="open"
        />
        <ReactTooltip id="open" place="top" type="dark" effect="solid" />
        </>
    )
}