import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeNote: this.props.activeNote,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeNote = { ...this.state.activeNote, [name]: value };

    this.setState({ activeNote });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Note</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="note-title">Title</Label>
              <Input
                type="text"
                id="note-title"
                name="title"
                value={this.state.activeNote.title}
                onChange={this.handleChange}
                placeholder="Enter Note Title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="note-description">Description</Label>
              <Input
                type="text"
                id="note-description"
                name="description"
                value={this.state.activeNote.description}
                onChange={this.handleChange}
                placeholder="Enter note description"
              />
            </FormGroup>
            <FormGroup check>
              <Label check>
                <Input
                  type="checkbox"
                  name="pinned"
                  checked={this.state.activeNote.pinned}
                  onChange={this.handleChange}
                />
                Pinned
              </Label>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeNote)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}