function request(query) {
    fetch(`/api/search?query=${query}`).
    then(res => console.log(res))
}

function getResults() {
    const query = document.getElementById("search-field")
    request(query)
}