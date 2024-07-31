// reducer.ts
export class Project {
  id: number;
  project_name: string;

  constructor(id: number, project_name: string) {
    this.id = id;
    this.project_name = project_name;
  }
}

const initialCounterState = {
  count: 0,
};

const initialProjectState = {
  projects: [] as Project[],
};

export const reducerCounter = (state = initialCounterState, action: any) => {
  switch (action.type) {
    // case "INC":
    //   return { ...state, count: state.count + 1 };
    // case "DEC":
    //   return { ...state, count: state.count - 1 };
    // case "RES":
    //   return { ...state, count: 0 };
    default:
      return state;
  }
};

export const reducerProject = (state = initialProjectState, action: any) => {
  switch (action.type) {
    // case "ADD_PROJECT":
    //   return { ...state, projects: [...state.projects, action.payload] };
    // case "REMOVE_PROJECT":
    //   return {
    //     ...state,
    //     projects: state.projects.filter(
    //       (project: Project) => project.id !== action.payload.id
    //     ),
    //   };
    default:
      return state;
  }
};
