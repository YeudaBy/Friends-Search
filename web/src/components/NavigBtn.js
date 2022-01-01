import { React, useState } from "react";
import ReactTooltip from 'react-tooltip';
import getStr from "../strings"
import {  } from 'react-icons/fa';


export function NextBtn(props) {
    return (
        <>
            <img
                className="navBtn"
                src="./nextBtn.png"
                onClick={props.handle}
                alt="next btn"
                data-tip={getStr("n-tip", props.sLang)}
                data-for="t-next"
            />
            <ReactTooltip id="t-next" place="right" type="dark" effect="solid" />
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
                data-tip={getStr("p-tip", props.sLang)}
                data-for="t-previous"
            />
            <ReactTooltip id="t-previous" place="left" type="dark" effect="solid" />
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

export function JumpTop(props) {

    const [visible, setVisible] = useState(false)

    const toggleVisible = () => {
        const scrolled = document.documentElement.scrollTop;
        if (scrolled > 300) {
            setVisible(true)
        }
        else if (scrolled <= 300) {
            setVisible(false)
        }
    };

    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };

    window.addEventListener('scroll', toggleVisible);

    return (
        <>
            <span onClick={scrollToTop}
                style={{ display: visible ? 'inline' : 'none' }} 
                className="scrollTop"
                data-tip={getStr("t-tip", props.sLang)}
                data-for="t-top"
                >
                &#8685;
            </span>
            <ReactTooltip id="t-top" place="top" type="dark" effect="solid" />

        </>
    );
}

