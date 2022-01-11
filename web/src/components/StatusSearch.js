import getStr from "../strings";

export function NoResults(props) {
    document.body.classList.remove("waiting")
    return (
        <div className="noResults">{getStr("no-res", props.sLang)}</div>
    )
}

export function Loading(props) {
    document.body.classList.add("waiting")
    return (
        <div className="loading">{getStr("loading", props.sLang)}</div>
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