import { Headline } from "./Headline"
import { NavBar } from "./TestNavBar"


export function Game(props) {
    return (
        <>
            <Headline />
            <NavBar sLang={props.sLang} updateSLang={props.updateSLang} />
            <p className="container">Game</p>
        </>
    )
}