import React, { Component } from "react";

class TextInput extends React.Component {
    constructor(props) {
      super(props);
      this.state = {value: ''};

      this.handleChange = this.handleChange.bind(this);
    //   this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      this.setState({value: event.target.value});
      console.log(event.target.value);
    }
  
    // handleSubmit(event) {
    //   alert('A name was submitted: ' + this.state.value);
    //   event.preventDefault();
    // }
  
    render() {
        const { placeholder } = this.props;
        return (
                <div className="TextInput">
                    <input autoComplete="false" style={{ border: '0', outline: 'none'}} placeholder={placeholder} type="text" value={this.state.value} onChange={this.handleChange} />
                </div>
        );
        }
    }

export default TextInput;