// Home.tsx
"use client";
import Link from "next/link";
import { useEffect, useState } from "react";
import Square from "./Square/page"; // Assuming Game component is in a separate file
import { Provider } from "react-redux";
import Counter from "./Counter/page";
import _Project from "./Project/page";
import store from "./Context/store";

import { NavLink } from "react-router-dom";
const Home = () => {
  if (!store) {
    return <div>Loading...</div>;
  }
  // const [isCounterOpen, setIsCounterOpen] = useState(false);
  return (
    <Provider store={store}>
      <div className="text-black dark:text-black flex flex-row justify-center items-center">
        <_Project />
      </div>
    </Provider>
  );
};

export default Home;
