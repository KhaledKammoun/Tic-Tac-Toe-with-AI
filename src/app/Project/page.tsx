"use client";
// _Project.tsx
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Project } from "../Context/reducer";
// import SubProject from "../SubProject/page";
import { RootState } from "../Context/store";

const _Project: React.FC = () => {
  const projects = useSelector(
    (state: RootState) => state?.projects?.projects || []
  );
  const dispatch = useDispatch();
  const [selectedProject, setSelectedProject] = useState<number | null>(null);

  const project_name: string | undefined =
    selectedProject !== null ? projects[selectedProject]?.project_name : "";

  const handleAddProject = () => {
    const newProject: Project = {
      id: Math.random(),
      project_name: `Project ${projects?.length + 1}`,
    };
    dispatch({ type: "ADD_PROJECT", payload: newProject });
  };

  const handleRemoveProject = () => {
    if (projects.length > 0) {
      dispatch({
        type: "REMOVE_PROJECT",
        payload: { id: projects[0]?.id },
      });
    }
  };

  return (
    <div>
      <div className="flex flex-row justify-center custom-button">
        <div onClick={handleAddProject}>Add Project</div>
        <div onClick={handleRemoveProject}>Remove Project</div>
      </div>
      {projects.length > 0 ? (
        projects.map((project: Project, index: number) => (
          <div
            key={project.id}
            className="text-5xl"
            onClick={() => setSelectedProject(index)}
          >
            {project.project_name}
          </div>
        ))
      ) : (
        <div className="text-5xl">No Project</div>
      )}
      {selectedProject !== null && <>Selected Project : {project_name}</>}
      {/* <SubProject /> */}
    </div>
  );
};

export default _Project;
