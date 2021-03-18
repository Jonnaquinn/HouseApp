import React from "react";
import { useManager, useManagerDispatch } from "../hooks/useManagerStore"

export default function Form() {
  const managerDispatch = useManagerDispatch();
  let { formSubmit, formClicked, iFrameClicked } = useManager();

  
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
    limit: "",
    radius: "",
    venuecategory: "",
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
      limit: "",
      radius: "",
      venuecategory: "",
    })
  }
  // function to make inputs read only when needed
  // if (formSubmit == true) {
  //   console.log(formSubmit)
  //   document.getElementById("minPrice").setAttribute("readOnly", true);
  // } else if (formSubmit == false) {
  //   document.getElementById("minPrice").removeAttribute("readonly");
  // }


  // React.useEffect(() => {
  //   setState(state);
  // }, [state]);

  function handleChange(e) {
    const value = e.target.value;
    setState({
      ...state,
      [e.target.name]: value
    });
    // console.log(e.target.name, value)
  }

  function handleSubmit() {
    fetch("/", {
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
              managerDispatch({ type: "submit", value: {formSubmit: true} })
              managerDispatch({ type: "submitClick" })
              // test1();
              // managerDispatch({ type: "iFrameClick", value: {iFrameClicked: true} })
            }}
        >
            Ok
            </div>
            <div className="cancel-button"
            onClick={() => {
              console.log("cancel button")
              managerDispatch({ type: "submit", value: {formSubmit: false} })
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
        <input id='minPrice' placeholder="-- Min Price --" type="text" autoComplete="none" name="minPrice" value={state.minPrice} onChange={handleChange}/>
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
      {/* {formSubmit && (
        <div>
            <hr style={{marginTop: '15px', marginBottom: '15px'}}></hr>
            <h1 className="title">Filter Listings</h1>
            <p className="description">
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type.
            </p>
            <hr style={{marginTop: '17px', marginBottom: '17px'}}></hr>
            <div className="TextInputHalfLeft">
              <input placeholder="-- Limit --" type="text" autoComplete="none" name="limit" value={state.limit} onChange={handleChange}/>
            </div>
            <div className="TextInputHalfRight">
              <input placeholder="-- Radius --" type="text" name="radius" value={state.radius} onChange={handleChange}/>
          </div>
          <div className="TextInput">
            <input placeholder="-- Venue Category --" type="text" autoComplete="none" name="venuecategory" value={state.venuecategory} onChange={handleChange}/>
          </div>
        </div>
      )} */}
      <Buttons></Buttons>
    </form>
  );
}
// export default Form;

// {/* <textarea name="bio" value={state.bio} onChange={handleChange} /> */}
