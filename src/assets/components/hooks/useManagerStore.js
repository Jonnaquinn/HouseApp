import makeStore from "./makeStore";

const initialState = {
    formSubmit: false,
    formClicked: false,
    iFrameClicked: false,
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
        case "iFrameClick":
            console.log(state.iFrameClicked)
            return {
                ...state,
                iFrameClicked: action.value.iFrameClicked,
            };
        default:
            throw new Error("Unknown action!", action);
    }
};

const [ManagerProvider, useManagerDispatch, useManager] = makeStore(managerReducer, initialState);

export { ManagerProvider, useManager, useManagerDispatch };
