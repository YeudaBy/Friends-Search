
export function NoResults() {
    document.body.classList.add("waiting") 
    return (
        <div className="noResults">No results was found!</div>
    )
}

export function Loading() {
    return (
        <div className="loading">Loading...!</div>
    )
}

export function Error(props) {
    document.body.classList.remove("waiting") 
    if (!props.error) {
        return null
    }
    return (
        <div className="error">{props.error}</div>
    )
}