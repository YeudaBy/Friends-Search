import React from "react";
import LinkBtn from "./LinkBtn"
import SelectLang from "./SelectLang";
import getStr from "../strings";
import { RiTelegramLine } from 'react-icons/ri';
import { VscCode } from "react-icons/vsc";
import { DiGithub } from "react-icons/di"
import { useMediaPredicate } from "react-media-hook";



export default function HeadNav(props) {

    const less422 = useMediaPredicate("(max-width: 422px)");

    return (
        <div className="headNav">
            <div className="Links">
                <LinkBtn
                    label={less422 ? <VscCode /> : "Api"}
                    url={"https://api.friends-search.com"}
                />
                <LinkBtn
                    label={less422 ? <DiGithub /> : "GitHub"}
                    url={"https://github.com/YeudaBy/Friends-Search"}
                />
                <LinkBtn
                    label={less422 ? <RiTelegramLine /> : "Telegram Bot"}
                    url={"https://t.me/Friends_SearchBot"}
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
