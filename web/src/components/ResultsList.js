import React from "react";
import { Result } from "./Result";
import { JumpTop } from "./NavigBtn"
import getStr from "../strings";


export default function ResultsList(props) {

    if (Object.keys(props.results).length > 0) {
        return (
            <div className="resultsList"
                dir={props.dir}>
                {props.results.map((e) =>
                    <Result
                        key={e.id} id={e.id} content={e.content} season={e.season}
                        episode={e.episode} start={e.start} end={e.end}
                        sLang={props.sLang}
                    />)}
                <JumpTop sLang={props.sLang}/>
            </div>
        )
    }
    else {
        return (
            <div className="noResults">
                {getStr("no-res", props.sLang)}
            </div>
        )
    }
}