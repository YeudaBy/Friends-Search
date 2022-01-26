// import { NavBar } from "./TestNavBar"
import { Logo } from "./Logo"

export default function HomeHeadline(props) {
    return (
        <div id="headline">
            <Logo size={"2em"}/>
            <h3>
                Aliqua cupidatat et ea labore irure commodo veniam.
                Velit dolor voluptate elit sunt proident.
            </h3>
        </div>
    )
}

export function Headline(props) {
    return (
        <header id="headerline">
            <Logo />
        </header>
    )
}