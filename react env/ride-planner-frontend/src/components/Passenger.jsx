import React from "react";
import "./Passenger.css"; // Import any necessary styles

function Passenger({ userId, name, addDriver, addPassenger }) {

  //const nameToID = (name) => name.replace(/\s+/g, "-").toLowerCase();
  //TODO: change depending on unassigned, driver, or in car

  return (
    <div id={userId} data-id={userId} className="passenger">
      <div className="passName">{name}</div>
      <div>
        <button className="passButton" onClick={() => addDriver(userId)}>
          <img className="passButtonImg" src="steer.svg" alt="Driver Icon" />
        </button>
        <button className="passButton" onClick={(event) => addPassenger(userId, event)}>
          <img className="passButtonImg" src="car.svg" alt="Passenger Icon" />
        </button>
      </div>
    </div>
  );
}

export default Passenger;