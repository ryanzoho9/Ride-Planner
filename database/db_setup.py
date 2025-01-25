import psycopg2

conn = psycopg2.connect(
    host="localhost", dbname="postgres", user="postgres", password="password", port=5432
)
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE users (
	user_id VARCHAR(255) PRIMARY KEY,
	CarOwn_id VARCHAR(255),
	CarGoInId VARCHAR(255),
	name VARCHAR(255),
	x_coord DOUBLE PRECISION,
	y_coord DOUBLE PRECISION,
	phone_number VARCHAR(20),
	event_id VARCHAR(255));

    CREATE TABLE cars (
        car_id VARCHAR(255),
        seats_available INT,
        passengers INT);

    CREATE TABLE events (
        event_id VARCHAR(255),
        event_name VARCHAR(255),
        description VARCHAR(255),
        start_date DATE,
        start_time TIME,
        x_coord DOUBLE PRECISION,
	    y_coord DOUBLE PRECISION,
        event_address VARCHAR(255));

    ALTER TABLE cars
    ADD CONSTRAINT fk_car UNIQUE (car_id);

    ALTER TABLE users
    ADD CONSTRAINT fk_car FOREIGN KEY (cargoinid)
    REFERENCES cars (car_id)
    ON DELETE CASCADE;

    ALTER TABLE events
    ADD CONSTRAINT fk_event UNIQUE (event_id);

    ALTER TABLE users
    ADD CONSTRAINT fk_event FOREIGN KEY (event_id)
    REFERENCES events (event_id)
    ON DELETE CASCADE;

    ALTER TABLE users
    ADD CONSTRAINT fk_carown FOREIGN KEY (carown_id)
    REFERENCES cars (car_id)
    ON DELETE CASCADE;
    """
)

conn.commit()
cur.close()
conn.close()
