import React, { useState } from "react";

/**
 * A React component that allows users to create a new event.
 * Submits event details to the Flask backend at /events/create_plan.
 */
function Create() {
  // Define form state
  const [formData, setFormData] = useState({
    event_name: "",
    description: "",
    start_date: "",
    start_time: "",
    event_address: "",
  });

  // Define error or success messages
  const [message, setMessage] = useState("");

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(""); // Clear previous messages

    try {
      // Prepare the data to match the backend’s expected fields
      const payload = {
        event_name: formData.event_name,
        description: formData.description,
        start_date: formData.start_date,
        start_time: formData.start_time,
        event_address: formData.event_address,
      };

      // Send POST request to the Flask endpoint
      // TODO: CHANGE LOCALHOST TO WHATEVER IS CORRECT
      const response = await fetch(
        "http://127.0.0.1:3002/api/events/create/create_plan",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(payload),
        }
      );

      const result = await response.json();

      if (!response.ok) {
        // Handle errors from the backend
        setMessage(`Error: ${result.error || "Unknown error occurred"}`);
      } else {
        // Success: The backend returns event_uuid in result
        setMessage(`Event created! ID: ${result.event_uuid}`);
        // Optionally reset the form
        setFormData({
          event_name: "",
          description: "",
          start_date: "",
          start_time: "",
          event_address: "",
        });
      }
    } catch (error) {
      // Handle network or unexpected errors
      setMessage(`Error: ${error.message}`);
    }
  };

  return (
    <div className="create-page">
      <h1>Create a new event</h1>
      <form onSubmit={handleSubmit}>
        {/* Event Name */}
        <div className="form-group">
          <label htmlFor="event_name">Event title:</label>
          <input
            type="text"
            id="event_name"
            name="event_name"
            value={formData.event_name}
            onChange={handleChange}
            required
          />
        </div>

        {/* Description */}
        <div className="form-group">
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            required
          />
        </div>

        {/* Date */}
        <div className="form-group">
          <label htmlFor="start_date">Date:</label>
          <input
            type="date"
            id="start_date"
            name="start_date"
            value={formData.start_date}
            onChange={handleChange}
            required
          />
        </div>

        {/* Time */}
        <div className="form-group">
          <label htmlFor="start_time">Time:</label>
          <input
            type="time"
            id="start_time"
            name="start_time"
            value={formData.start_time}
            onChange={handleChange}
            required
          />
        </div>

        {/* Location */}
        <div className="form-group">
          <label htmlFor="event_address">Location:</label>
          <input
            type="text"
            id="event_address"
            name="event_address"
            value={formData.event_address}
            onChange={handleChange}
            required
          />
        </div>

        {/* Submit Button */}
        <button type="submit">Create Event</button>
      </form>

      {/* Display any feedback messages */}
      {message && <p>{message}</p>}
    </div>
  );
}

export default Create;
