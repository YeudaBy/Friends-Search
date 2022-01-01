import React from "react";
import LinkBtn from "./LinkBtn"
import SelectLang from "./SelectLang";
import getStr from "../strings";

export default function HeadNav(props) {
    return (
        <div className="headNav">
            <div className="Links">
                <LinkBtn
                    label={"Api"}
                    url={"/api"}
                />
                <LinkBtn
                    label={"GitHub"}
                    url={"https://github.com/YeudaBy/Friends-Search"}
                />
                {/* <LinkBtn
                    label={"Game"}
                    url={"/game"}
                /> */}
                <LinkBtn
                    label={"Telegram Bot"}
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
