import React, { useEffect, useState } from "react";
import Passenger from "./Passenger";
import CarGroup from "./CarGroup";

const Rides = ({ webSocket }) => {
  const [data, setData] = useState({ unassigned: [], cars: [] });

  useEffect(() => {
    const handleMessage = (event) => {
      const updatedData = JSON.parse(event.data);
      setData(updatedData);
    };

    webSocket.addEventListener("message", handleMessage);

    return () => {
      webSocket.removeEventListener("message", handleMessage);
    };
  }, [webSocket]);

  const sendAction = (type, payload) => {
    webSocket.send(JSON.stringify({ type, ...payload }));
  };

  return (
    <main>
      <div id="groups">
        {data.cars.map((car) => (
          <CarGroup
            key={car.driver}
            driver={car.driver}
            passengers={car.passengers}
            sendAction={sendAction}
          />
        ))}
      </div>

      <p style={{ marginTop: "30px" }}>Unassigned</p>
      <div id="unassigned">
        {data.unassigned.map((id) => (
          <Passenger
            key={id}
            id={id}
            role="unassigned"
            sendAction={sendAction}
            availableDrivers={data.cars.filter(
              (car) => car.passengers.length < 4
            ).map((car) => car.driver)}
          />
        ))}
      </div>
    </main>
  );
};

export default Rides;
