import { Link } from "react-router-dom"
import "../"

export function Logo(props) {
    return (
        <Link to={"/"} className="logo blurBg">
            <TextLogo size={props.size}/>
        </Link>
    )
}

export function TextLogo(props) {
    return (
        <h1
            className="notranslate"
            id="textLogo"
            style={
                typeof props.size === "undefined" ?
                    { "fontSize": "20px" } : { "fontSize": props.size }
            }
        >
            {"F"}
            <span className="red">•</span>
            {"r"}
            <span className="blue">•</span>
            {"i"}
            <span className="yelow">•</span>
            {"e"}
            <span className="red">•</span>
            {"n"}
            <span className="yelow">•</span>
            {"d"}
            <span className="blue">•</span>
            {"s"}{" "}
            {"Search"}
        </h1>
    )
}