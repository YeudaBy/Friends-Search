import React from "react";

export default function SearchField(props) {
    return (
        <div className="searchField center">
           <form className="searchForm" onSubmit={props.handleSubmit}>
                <input type="search" name="search" value={props.value} onChange={props.searchChange} className="searchInput"/>
                {props.value !== "" && <><br /><input type="submit" value="Search" className="searchBtn"/></>}
            </form>
        </div>
    )
}