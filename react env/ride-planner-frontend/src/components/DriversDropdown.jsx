import React from 'react';

const DriversDropdown = ({ options, onSelect }) => {
  return (
    <div className="dropdown-content">
      {options.map((option) => (
        <button key={option} onClick={() => onSelect(option)}>
          {option}
        </button>
      ))}
    </div>
  );
};

export default DriversDropdown;
