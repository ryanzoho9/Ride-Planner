import { useState } from 'react'

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./pages/Home.jsx"
import Create from "./pages/Create.jsx"
import Event from "./pages/Event.jsx"
//import Rides from "./pages/Rides.jsx"
function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/create" element={<Create />} />
        <Route path="/event" element={<Event />} />
      </Routes>
    </Router>
  )
}

export default App
