"use client";
import React from "react";
import { useDispatch, useSelector } from "react-redux";

interface CounterState {
  count: number;
}

function Counter() {
  const { count }: CounterState = useSelector((state: any) => state.counter);
  const dispatchCounter = useDispatch();

  return (
    <div>
      <div>Counter: {count}</div>
      <div>
        <div onClick={() => dispatchCounter({ type: "INC" })}>INCREMENT</div>
        <div onClick={() => dispatchCounter({ type: "DEC" })}>DECREMENT</div>
        <div onClick={() => dispatchCounter({ type: "RES" })}>RESET</div>
      </div>
    </div>
  );
}

export default Counter;
