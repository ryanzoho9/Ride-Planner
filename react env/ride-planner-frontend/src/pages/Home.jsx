import React, { useState } from "react";
import "../styles/create.css";

function Home() {
  

  return (
    <div className="home-page">
      <h1>Ride Planner</h1>
      <p>Event planning and ride coordination made easy.</p>
        
      <a href="/create">Create a new event</a>
    </div>
  );
}

export default Home;
