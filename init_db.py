import sqlite3

def init_tables():
	conn = sqlite3.connect("can_db.db")
	cursor = conn.cursor()

	# Table for each sensor/can_device
	tables = ["bmu_heartbeat_sensor", "pack_state_of_charge", "something"]

	# Master table for all devices on the can network
	cursor.execute(f"""
	CREATE TABLE IF NOT EXISTS can_devices (
		can_id TEXT PRIMARY KEY,
		description TEXT
	);
	""")

	for table in tables:
		cursor.execute(f"""
		CREATE TABLE IF NOT EXISTS {table} (
			timestamp DATETIME PRIMARY KEY DEFAULT CURRENT_TIMESTAMP,
			can_id TEXT NOT NULL,
			raw TEXT NOT NULL,
			FOREIGN KEY (can_id) REFERENCES can_devices(can_id)
		);
		""")
	conn.commit()
	conn.close()
