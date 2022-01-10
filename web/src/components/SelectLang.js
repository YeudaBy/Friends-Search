import Form from "react-bootstrap/Form"

export default function SelectLang(props) {
    return (
        <>
            <Form.Select aria-label="Default select example" onChange={props.updateLang}>
                <option value="ag">Search with all available languages</option>
                <option value="en">English</option>
                <option value="he">עברית</option>
                <option value="fr">Français</option>
            </Form.Select>
        </>
    )
}