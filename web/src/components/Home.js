import Head from "./Head"
import Search from "./Search"

export function Home(props) {
    return (
        <div className={props.sLang}>
            <Head sLang={props.sLang} updateSLang={props.updateSLang} />
            <Search sLang={props.sLang} />
        </div>
    )
}