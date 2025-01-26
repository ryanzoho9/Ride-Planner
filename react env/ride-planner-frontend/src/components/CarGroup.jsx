import React from "react";
import PassengerCard from "./PassengerCard.jsx";

const CarGroup = ({ driver, passengers, sendAction }) => {
  return (
    <div className="car">
      <PassengerCard id={driver} role="driver" sendAction={sendAction} />
      {passengers.map((passenger) => (
        <PassengerCard
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
