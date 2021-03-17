import makeStore from "./makeStore";

const initialState = {
    formSubmit: false,
    formClicked: false,
};

const managerReducer = (state, action) => {
    switch (action.type) {
        case "reset":
            return initialState;
        case "submit":
            return {
                ...state,
                formSubmit: action.value.formSubmit,
            };
        case "submitClick":
            console.log(state.formClicked)
            return {
                ...state,
                formClicked: !state.formClicked,
            };
        default:
            throw new Error("Unknown action!", action);
    }
};

const [ManagerProvider, useManagerDispatch, useManager] = makeStore(managerReducer, initialState);

export { ManagerProvider, useManager, useManagerDispatch };
