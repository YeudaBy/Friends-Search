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
                    label={"Test"}
                    url={"https://google.com"}
                />
            </div>

            <SelectLang
                label={"Select site lang"}
                changeLang={props.updateLang}
                value={props.lang}
            />
        </div>
    )
}