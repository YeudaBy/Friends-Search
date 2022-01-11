import Form from "react-bootstrap/Form"
import { MdOutlineLanguage } from "react-icons/md"

export default function SelectLang(props) {
    return (
        <div className="searchLang">
            <Form.Select onChange={props.updateSearchLang} value={props.value}>
                <option value="ag">all available languages</option>
                <option value="en">English</option>
                <option value="he">עברית</option>
                <option value="fr">Français</option>
            </Form.Select>
            <label className="searchLabel">{<MdOutlineLanguage />} Search with language: </label>

        </div>
    )
}