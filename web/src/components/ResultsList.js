import React from "react";
import { Result } from "./Result";
import { JumpTop } from "./NavigBtn"


export default function ResultsList(props) {

    document.body.classList.remove("waiting");
    return (
        <div className="resultsList">
            <>Show {props.count} Results:</>
            {props.results.map((e) =>
                <Result
                    key={e.id} id={e.id} content={e.content} season={e.season}
                    episode={e.episode} start={e.start} end={e.end}
                    sLang={props.sLang}
                />)}
            <JumpTop sLang={props.sLang} />
        </div>
    )
}