import React from "react";

function Form() {
  let [state, setState] = React.useState({
    level: "sale",
    minPrice: "",
    maxPrice: "",
    state: "",
    suburb: "",
    postcode: "",
    minBed: "",
    maxBed: "",
    minBath: "",
    maxBath: "",
    minParks: "",
    maxParks: "",
    surroundingsuburbs: "False",
    surround: "",
  })

  function reset() {
    setState({
      level: "sale",
      minPrice: "",
      maxPrice: "",
      state: "",
      suburb: "",
      postcode: "",
      minBed: "",
      maxBed: "",
      minBath: "",
      maxBath: "",
      minParks: "",
      maxParks: "",
      surroundingsuburbs: "False",
      surround: "",
    })
  }

  // React.useEffect(() => {
  //   setState(state);
  // }, [state]);

  function handleChange(e) {
    const value = e.target.value;
    setState({
      ...state,
      [e.target.name]: value
    });
    console.log(e.target.name, value)
  }

  function handleSubmit() {
    console.log("making request")
    fetch("/result", {
      method: "POST",
      cache: "no-cache",
      headers: {
        "content_type":"application/json",
        'Accept': 'application/json'
      },
      body:JSON.stringify(state)
    })
  }

  function Buttons() {
    // do somthing
  
    return (
        <div className="panel-buttons">
            <div className="ok-button"
            onClick={() => {        
              console.log("ok button")
              console.log(JSON.stringify(state))
              handleSubmit();
            }}
        >
            Ok
            </div>
            <div className="cancel-button"
            onClick={() => {
              console.log("cancel button")
              reset();
            }}
        >
            Cancel
            </div>
        </div>
    )
  }

  return (
    <form autoComplete="none">
      <div className="RadioButton">
        <label>
          Sale
          <input type="radio" name="level" value="sale" checked={state.level === "sale"} onChange={handleChange}/>
        </label>
        <label>
          Rent
          <input type="radio" name="level" value="rent" checked={state.level === "rent"} onChange={handleChange}
          />
        </label>
      </div>
      <div className="TextInputHalfLeft">
        <input placeholder="-- Min Price --" type="text" autoComplete="none" name="minPrice" value={state.minPrice} onChange={handleChange}/>
      </div>
      <div className="TextInputHalfRight">
        <input placeholder="-- Max Price --" type="text" name="maxPrice" value={state.maxPrice} onChange={handleChange}/>
      </div>
      <div className="TextInput">
        <input placeholder="-- State --" type="text" autoComplete="none" name="state" value={state.state} onChange={handleChange}/>
      </div>
      <div className="TextInput">
        <input placeholder="-- Suburb --" type="text" autoComplete="none" name="suburb" value={state.suburb} onChange={handleChange}/>
      </div>
      <div className="TextInput">
        <input placeholder="-- PostCode --" type="text" autoComplete="none" name="postcode" value={state.postcode} onChange={handleChange}/>
      </div>
      <div className="TextInputHalfLeft">
        <input placeholder="-- Min Beds --" type="text" name="minBed" value={state.minBed} onChange={handleChange}/>
      </div>
      <div className="TextInputHalfRight">
        <input placeholder="-- Max Beds --" type="text" name="maxBed" value={state.maxBed} onChange={handleChange}/>
      </div>
      <div className="TextInputHalfLeft">
        <input placeholder="-- Min Baths --" type="text" name="minBath" value={state.minBath} onChange={handleChange}/>
      </div>
      <div className="TextInputHalfRight">
        <input placeholder="-- Max Baths --" type="text" name="maxBath" value={state.maxBath} onChange={handleChange}/>
      </div>
      <div className="TextInputHalfLeft">
        <input placeholder="-- Min Parks --" type="text" name="minParks" value={state.minParks} onChange={handleChange}/>
      </div>
      <div className="TextInputHalfRight">
        <input placeholder="-- Max Parks --" type="text" name="maxParks" value={state.maxParks} onChange={handleChange}/>
      </div>
      <p className="description">
        Include Surrounding Suburbs In Your Search?
      </p>
      <div className="RadioButton" style={{marginLeft: '-11%'}}>
        <label>
          Yes
          <input type="radio" name="surroundingsuburbs" value="True" checked={state.surroundingsuburbs === "True"} onChange={handleChange}/>
        </label>
        <label>
          No
          <input type="radio" name="surroundingsuburbs" value="False" checked={state.surroundingsuburbs === "False"} onChange={handleChange}
          />
        </label>
      </div>
      {state.surroundingsuburbs === "True" && (
        <div className="TextInput" style={{marginTop: '10px'}}>
          <input placeholder="  -- Radius in Metres --" type="text" autoComplete="none" name="surround" value={state.surround} onChange={handleChange}/>
      </div>
      )}
      <Buttons></Buttons>
    </form>
  );
}
export default Form;

// {/* <textarea name="bio" value={state.bio} onChange={handleChange} /> */}
