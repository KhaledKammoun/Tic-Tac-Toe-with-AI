"use client";
import React, { useReducer } from "react";
import { useDispatch, useSelector } from "react-redux";

function SubProject() {
  const { count } = useSelector((state: any) => state.counter);
  const dispatchCounter = useDispatch();

  console.log(count);

  return (
    <div>
      <div>Final Count = {count}</div>
      <div>
        <div onClick={() => dispatchCounter({ type: "INC" })}>INC</div>
      </div>
    </div>
  );
}

export default SubProject;
