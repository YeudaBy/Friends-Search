import { Search } from "./components/Search";
import Head from "./components/Head";
import "./App.css"
import { useState } from "react";

function App() {
  const [lang, setLangs] = useState(0);

  function updateLang(newLang) { setLangs(newLang) }

  return (
    <>
      <Head lang={lang} updateLang={this.updateLang()}/>
      <Search lang={lang}/>
    </>
  );
}

export default App;
