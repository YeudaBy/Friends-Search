import React from "react";
import LinkBtn from "./LinkBtn"

export default function HeadNav(props) {
    return (
        <div className="headNav">
            <LinkBtn
                labek={"Api"}
                url={"/api"}
            />
        </div>
    )
}