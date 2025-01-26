import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Event() {
  const queryParameters = new URLSearchParams(window.location.search);
  const id = queryParameters.get("id");
  const [eventInfo, setEventInfo] = useState(null); // State for event info
  const [attendees, setAttendees] = useState([]); // State for attendees
  const [loadingEvent, setLoadingEvent] = useState(true); // Loading state for event info
  const [loadingAttendees, setLoadingAttendees] = useState(true); // Loading state for attendees
  const [error, setError] = useState(null); // State for errors

  useEffect(() => {
    console.log("EVENT ID ->>>>>>>>>>>>" + id);
    if (!id) {
      console.error("No id provided in URL");
      setError("Invalid event ID");
      setLoadingEvent(false);
      return;
    }

    const url = `http://127.0.0.1:3002/api/events/create/get_event?eventId=${id}`;
    console.log("Fetching event info from:", url);

    fetch(url)
      .then((response) => {
        console.log("Event info response status:", response.status);
        if (!response.ok) throw new Error("Failed to fetch event info");
        return response.json();
      })
      .then((data) => {
        console.log("Fetched event data:", data);
        setEventInfo(data);
        setLoadingEvent(false);
      })
      .catch((err) => {
        console.error("Error fetching event info:", err.message);
        setError(err.message);
        setLoadingEvent(false);
      });
  }, [id]);

  useEffect(() => {
    if (!id) {
      console.error("No id provided in URL");
      setError("Invalid event ID");
      setLoadingAttendees(false);
      return;
    }

    const url = `http://127.0.0.1:3002/api/events/create/get_event_attendees?eventId=${id}`;
    console.log("Fetching attendees from:", url);

    fetch(url)
      .then((response) => {
        console.log("Attendees response status:", response.status);
        if (!response.ok) throw new Error("Failed to fetch attendees");
        return response.json();
      })
      .then((data) => {
        console.log("Fetched attendees data:", data);
        setAttendees(data);
        setLoadingAttendees(false);
      })
      .catch((err) => {
        console.error("Error fetching attendees:", err.message);
        setError(err.message);
        setLoadingAttendees(false);
      });
  }, [id]);

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
          <p>
            <strong>Date:</strong> {eventInfo.start_date}
          </p>
          <p>
            <strong>Time:</strong> {eventInfo.start_time}
          </p>
          <p>
            <strong>Location:</strong> {eventInfo.event_address}
          </p>
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
