import strings from "./strings.json"

function getStr(msg = "msg-error", lang = "en") {
    return strings[msg][lang]
}

export default getStr;