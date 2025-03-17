import React, { useEffect, useState } from "react";
import axios from "axios";
import NoteForm from "./components/NoteForm";
import NoteList from "./components/NoteList";


function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/notes")
      .then(response => {
        setNotes(response.data);
      })
      .catch(console.error);
  }, []);

  const addNote = (note) => {
    axios.post("http://127.0.0.1:8000/notes", {
      text: note.text,
      tag: note.tag,
    })
      .then(response => {
        setNotes(response.data);
      })
      .catch(console.error);

  };


  return(
    <div>
      <h1>Notes</h1>
      <NoteForm addNote={addNote}/>
      <NoteList notes={notes}/>
    </div>
  )

}

export default App;
