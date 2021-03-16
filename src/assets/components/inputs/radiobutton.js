import React, { Component } from "react";

class RadioButton extends Component {
  constructor() {
    super();
    this.state = {
      name: "React"
    };
    this.onChangeValue = this.onChangeValue.bind(this);
  }

  onChangeValue(event) {
    console.log(event.target.value);
  }

  render() {
    const { label1, label2 } = this.props;
    return (
      <div className="RadioButton" onChange={this.onChangeValue}>
        <input className='radio' type="radio" value="1" name="type" /><label for="first">{label1}</label>
        {/* <br></br> */}
        <input className='radio' type="radio" value="2" name="type" /><label for="second">{label2}</label>
      </div>
    );
  }
}

export default RadioButton;