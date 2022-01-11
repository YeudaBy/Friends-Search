import Form from "react-bootstrap/Form"

export default function SelectSiteLang(props) {
    return (
        <>
            <Form.Select aria-label="Default select example" onChange={props.updateSLang} value={props.sLang}>
                <option value="en">Select SIte Language</option>
                <option value="en">English</option>
                <option value="he">עברית</option>
                <option value="fr">Français</option>
            </Form.Select>
        </>
    )
}