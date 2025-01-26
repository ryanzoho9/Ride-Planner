import React from 'react';

const PersonCard = ({ userId, name, isDriver, onAddDriver, onRemoveDriver, onAddPassenger, onRemovePassenger }) => {
  return (
    <div id={userId} data-name={name} className="passenger">
      <div className="passName">{name}</div>
      <div style={{ position: 'relative', display: 'inline-block' }}>
        {isDriver ? (
          <button className="passButton" onClick={() => onRemoveDriver(userId)}>
            <img className="passButtonImg" src="remove.svg" alt="Remove Driver" />
          </button>
        ) : (
          <>
            <button className="passButton" onClick={() => onAddDriver(userId)}>
              <img className="passButtonImg" src="steer.svg" alt="Add as Driver" />
            </button>
            <button className="passButton" onClick={(e) => onAddPassenger(userId, e)}>
              <img className="passButtonImg" src="car.svg" alt="Assign Passenger" />
            </button>
          </>
        )}
        {!isDriver && (
          <button className="passButton" onClick={() => onRemovePassenger(userId)}>
            <img className="passButtonImg" src="remove.svg" alt="Remove Passenger" />
          </button>
        )}
      </div>
    </div>
  );
};

export default PersonCard;
