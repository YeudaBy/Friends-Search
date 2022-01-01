import React from "react";
import LinkBtn from "./LinkBtn"
import SelectLang from "./SelectLang";
import getStr from "../strings";
import { FaTelegram, FaGithub, FaHtml5 } from 'react-icons/fa';
import { useMediaPredicate } from "react-media-hook";



export default function HeadNav(props) {

    const less422 = useMediaPredicate("(max-width: 422px)");

    return (
        <div className="headNav">
            <div className="Links">
                <LinkBtn
                    label={less422 ? <FaHtml5 /> : "Api"}
                    url={"/api"}
                />
                <LinkBtn
                    label={less422 ? <FaGithub /> : "GitHub"}
                    url={"https://github.com/YeudaBy/Friends-Search"}
                />
                {/* <LinkBtn
                    label={"Game"}
                    url={"/game"}
                /> */}
                <LinkBtn
                    label={less422 ? <FaTelegram /> : "Telegram Bot"}
                    url={"t.me/"}
                />
            </div>

            <div className="siteLang">
                <SelectLang
                    label={getStr("slng-site", props.sLang)}
                    updateLang={props.updateLang}
                    sLang={props.sLang}
                />
            </div>
        </div>
    )
}
