import React from "react";
import HelloWorld from "./HelloWorld";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function Home() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<HelloWorld />} />
        {/* Add more routes as needed */}
      </Routes>
    </Router>
  );
}

export default Home;
