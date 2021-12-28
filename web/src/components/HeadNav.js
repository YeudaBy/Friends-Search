import React from "react";
import LinkBtn from "./LinkBtn"
import SelectLang from "./SelectLang";

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
                    url={"https://google.com"}
                />
                <LinkBtn 
                    label={"Game"}
                    url={"/game"}
                />
                <LinkBtn 
                    label={"Telegram Bot"}
                    url={"t.me/"}
                />
            </div>

            <SelectLang
                label={"Select site lang"}
                updateLang={props.updateLang}
                value={props.value}
            />
        </div>
    )
}
