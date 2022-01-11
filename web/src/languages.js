import strings from "./strings.json"

export function supportedLanguages() {
    return strings.languages
}

export function browserLanguage() {
    const browsLang = window.navigator.userLanguage || window.navigator.language;
    let pureBrowsLang = /(\w{2,3})(-\w{2,3})?/.exec(browsLang)[1]
    const isSupported = Object.keys(supportedLanguages()).includes(pureBrowsLang)
    if (isSupported === 0 | isSupported === false) {
        pureBrowsLang = "en"
    }
    return pureBrowsLang
}