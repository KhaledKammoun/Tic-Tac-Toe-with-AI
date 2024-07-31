"use client";
import React from "react";
import { useDispatch, useSelector } from "react-redux";

interface CounterState {
  count: number; // Define the type for counter
}

function Counter() {
  const { count }: CounterState = useSelector((state: any) => state.counter); // Adjusted type
  const dispatchCounter = useDispatch();
  console.log(count);
  return (
    <div className="flex flex-col">
      <div className="font-bold text-lg text-gray-700 dark:text-gray-600">
        Counter: {count}
      </div>

      <div className="flex flex-row custom-button">
        <div onClick={() => dispatchCounter({ type: "INC" })}>INCREMENT</div>
        <div onClick={() => dispatchCounter({ type: "DEC" })}>DECREMENT</div>
        <div onClick={() => dispatchCounter({ type: "RES" })}>RESET</div>
      </div>
    </div>
  );
}

export default Counter;
