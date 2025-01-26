import React from "react";
import Passenger from "./Passenger";

const CarGroup = ({ driver, passengers, sendAction }) => {
  return (
    <div className="car">
      <Passenger id={driver} role="driver" sendAction={sendAction} />
      {passengers.map((passenger) => (
        <Passenger
          key={passenger}
          id={passenger}
          role="passenger"
          sendAction={sendAction}
        />
      ))}
    </div>
  );
};

export default CarGroup;
