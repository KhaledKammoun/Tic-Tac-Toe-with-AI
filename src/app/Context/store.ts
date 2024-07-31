// store.ts
import { legacy_createStore as createStore, combineReducers } from "redux";
import { reducerCounter, reducerProject } from "./reducer";

const rootReducer = combineReducers({
  counter: reducerCounter,
  projects: reducerProject,
});

export type RootState = ReturnType<typeof rootReducer>;

const store = createStore(rootReducer);

export default store;
