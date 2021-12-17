import React from "react";
import { Result } from "./Result";


export default function ResultsList(props) {
    return (
        <div className="resultsList"
            dir={props.dir}>
            {props.results.map((e) =>
                <Result
                    key={e.id} id={e.id} content={e.content} season={e.season}
                    episode={e.episode} start={e.start} end={e.end}
                />)}
        </div>
    )
}