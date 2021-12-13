import React from "react";
import ReactTooltip from 'react-tooltip';

export function NextBtn(props) {
    return (
        <>
            <img
                className="navBtn"
                src="./nextBtn.png"
                onClick={props.handle}
                alt="next btn"
                data-tip="Next sentence"
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
                data-tip="previous btn"
                data-for="previous"
            />
            <ReactTooltip id="previous" place="left" type="dark" effect="solid" />
            </>
    )
}

// export function openBtn(props) {
//     return (

//     )
// }