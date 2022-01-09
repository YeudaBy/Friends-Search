import React from "react";
import { Result } from "./Result";
import { JumpTop } from "./NavigBtn"


export default function ResultsList(props) {

    document.body.classList.remove("waiting");
    return (
        <div className="resultsList"
            dir={props.dir}>
            <>Show {props.results.count} Results:</>
            {props.results.resultsList.map((e) =>
                <Result
                    key={e.id} id={e.id} content={e.content} season={e.season}
                    episode={e.episode} start={e.start} end={e.end}
                    sLang={props.sLang}
                />)}
            <JumpTop sLang={props.sLang} />
        </div>
    )
}