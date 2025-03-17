import { useEffect, useState } from "react";
import Header from "./components/Header";
import { getNotes } from "./components/NotesApp";
import NoteForm from "./components/NoteForm";
import NoteList from "./components/NoteList";
function App() {
  const [notes, setNotes] = useState([]);

  useEffect(() => {
    getNotes()
    .then((data) =>setNotes(data))
    .catch(console.error);
    
  }, []);


  return (
    <div className="container">
      <Header />
      <div className="notes-container">
        <NoteForm setNotes={setNotes}/>
        <NoteList
          notes={notes}
        />

      </div>
    </div>
  );
}

export default App;
