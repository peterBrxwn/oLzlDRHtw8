import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      notes: [],
      modal: false,
      activeNote: {
        title: "",
        description: "",
        pinned: false,
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/notes/")
      .then((res) => this.setState({ notes: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  submitNote = (note) => {
    this.toggle();

    if (note.id) {
      axios
        .put(`/api/notes/${note.id}/`, note)
        .then((res) => this.refreshList());
      return;
    }
    axios.post("/api/notes/", note).then((res) => this.refreshList());
  };

  deleteNote = (note) => {
    axios.delete(`/api/notes/${note.id}/`).then((res) => this.refreshList());
  };

  createNote = () => {
    const note = { title: "", description: "", pinned: false };

    this.setState({ activeNote: note, modal: !this.state.modal });
  };

  editNote = (note) => {
    this.setState({ activeNote: note, modal: !this.state.modal });
  };

  handleLogout = () => {};

  renderNotes = () => {
    return this.state.notes.map((note, index) => (
      <>
        <li
          key={note.id}
          className={`list-group-item d-flex justify-content-between align-items-center ${note.pinned ? 'bg-warning' : 'bg-white'}`}
        >
          <div className="d-flex flex-column">
            <strong>{note.title}{note.pinned && <span className="me-2">📌</span>}</strong>
            <small>{note.description.substring(0, 100)}{note.description.length > 100 ? '...' : ''}</small>
          </div>
          <span className="d-flex align-items-center">
            <button
              className="btn btn-outline-warning me-2"
              onClick={() => this.togglePin(note)}
            >
              {note.pinned ? 'Unpin' : 'Pin'}
            </button>
            <button
              className="btn btn-secondary me-2"
              onClick={() => this.editNote(note)}
            >
              Edit
            </button>
            <button
              className="btn btn-danger"
              onClick={() => this.deleteNote(note)}
            >
              Delete
            </button>
          </span>
        </li>
      </>
    ));
  };

  render() {
    return (
      <>
        <nav className="navbar navbar-dark bg-dark">
          <div className="container-fluid">
            <button className="btn btn-danger ms-auto" onClick={this.handleLogout}>
              Logout
            </button>
          </div>
        </nav>
        <main className="container">
          <h1 className="text-white text-uppercase text-center my-4">
            Notes app
          </h1>
          <div className="row">
            <div className="col-lg-6 col-md-8 col-sm-10 mx-auto p-0">
              <div className="card p-3">
                <ul className="list-group list-group-flush border-top-0">
                  {this.renderNotes()}
                </ul>
              </div>
            </div>
          </div>
          {this.state.modal ? (
            <Modal
              activeNote={this.state.activeNote}
              toggle={this.toggle}
              onSave={this.submitNote}
            />
          ) : null}
        </main>
        <button
        className="btn btn-primary rounded-circle position-fixed bottom-0 end-0 m-4"
        style={{ width: '60px', height: '60px', fontSize: '24px' }}
        onClick={this.createNote}
      >
        +
      </button>
      </>
    );
  }
}

export default App;
