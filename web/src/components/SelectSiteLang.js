import Dropdown from "react-bootstrap/Dropdown"

export default function SelectSiteLang(props) {
    return (
        <>
            <Dropdown>
                <Dropdown.Toggle variant="success" id="dropdown-basic">
                    Select Site Language
                </Dropdown.Toggle>

                <Dropdown.Menu className="siteSelectLangList">
                        <Dropdown.Item onClick={props.updateLang} data-key={"he"} className="langItem">עברית</Dropdown.Item>
                        <Dropdown.Item onClick={props.updateLang} data-key={"en"} className="langItem">English</Dropdown.Item>
                        <Dropdown.Item onClick={props.updateLang} data-key={"fr"} className="langItem">Français</Dropdown.Item>
                </Dropdown.Menu>
            </Dropdown>
        </>
    )
}