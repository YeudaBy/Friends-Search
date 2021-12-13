import React from "react";

export default function SearchField(props) {
    return (
        <div className="searchField">
           <form className="searchForm" onSubmit={props.handleSubmit}>
                <input type="search" name="search" value={props.value} onChange={props.searchChange}/>
                {props.value !== "" && <input type="submit" value="Search" />}

                {/* <select value={props.value} onChange={props.langChange}> */}
                    {/* {} */}
                {/* </select> */}
            </form>
        </div>
    )
}