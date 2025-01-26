import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Event() {
  const { eventId } = useParams(); // Get the event ID from the URL
  const [eventInfo, setEventInfo] = useState(null); // State for event info
  const [attendees, setAttendees] = useState([]); // State for attendees
  const [loadingEvent, setLoadingEvent] = useState(true); // Loading state for event info
  const [loadingAttendees, setLoadingAttendees] = useState(true); // Loading state for attendees
  const [error, setError] = useState(null); // State for errors

  // Fetch event info using the event ID
  useEffect(() => {
    fetch(`http://localhost:5000/api/event/${eventId}`)
      .then((response) => {
        if (!response.ok) throw new Error("Failed to fetch event info");
        return response.json();
      })
      .then((data) => {
        setEventInfo(data);
        setLoadingEvent(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoadingEvent(false);
      });
  }, [eventId]); // Re-fetch if eventId changes

  // Fetch attendee list using the event ID
  useEffect(() => {
    fetch(`http://localhost:5000/api/event/${eventId}/attendees`)
      .then((response) => {
        if (!response.ok) throw new Error("Failed to fetch attendees");
        return response.json();
      })
      .then((data) => {
        setAttendees(data);
        setLoadingAttendees(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoadingAttendees(false);
      });
  }, [eventId]); // Re-fetch if eventId changes

  // Handle Ride Planner button click
  const openRidePlanner = () => {
    alert("Ride planner is opening...");
    // Implement your ride planner functionality here
  };

  // Loading state
  if (loadingEvent || loadingAttendees) return <p>Loading...</p>;

  // Error state
  if (error) return <p>Error: {error}</p>;

  return (
    <div style={styles.container}>
      {/* Event Info Section */}
      {eventInfo && (
        <div style={styles.eventInfo}>
          <h1>{eventInfo.name}</h1>
          <p>{eventInfo.description}</p>
          <p><strong>Date:</strong> {eventInfo.date}</p>
          <p><strong>Time:</strong> {eventInfo.time}</p>
          <p><strong>Location:</strong> {eventInfo.location}</p>
        </div>
      )}

      {/* Ride Planner Button */}
      <div style={styles.buttonContainer}>
        <button style={styles.ridePlannerButton} onClick={openRidePlanner}>
          Open Ride Planner
        </button>
      </div>

      {/* Attendees List */}
      <div style={styles.attendeesSection}>
        <h2>Attendees</h2>
        <ul style={styles.attendeesList}>
          {attendees.map((attendee) => (
            <li key={attendee.id} style={styles.attendeeItem}>
              {attendee.name}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Event;

// Inline styles
const styles = {
  container: {
    padding: "20px",
    fontFamily: "Arial, sans-serif",
  },
  eventInfo: {
    marginBottom: "20px",
    padding: "15px",
    border: "1px solid #ddd",
    borderRadius: "8px",
    backgroundColor: "#f9f9f9",
  },
  buttonContainer: {
    textAlign: "center",
    marginBottom: "20px",
  },
  ridePlannerButton: {
    padding: "10px 20px",
    fontSize: "16px",
    backgroundColor: "#007bff",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
  attendeesSection: {
    marginTop: "20px",
  },
  attendeesList: {
    listStyle: "none",
    padding: "0",
  },
  attendeeItem: {
    padding: "10px",
    borderBottom: "1px solid #ddd",
  },
};
