import React from "react";
import getStr from "../strings";

export default function SearchField(props) {
    return (
        <div className="searchField center">
            <form className="searchForm" onSubmit={props.handleSubmit}>
                <input type="search"
                    name="search"
                    value={props.value}
                    onChange={props.searchChange}
                    className="searchInput"
                    placeholder="Unagi..." />
                {props.value !== "" && <><br /><input
                    type="submit"
                    value={getStr("search-btn", props.sLang)}
                    className="searchBtn" /></>}
            </form>
        </div>
    )
}