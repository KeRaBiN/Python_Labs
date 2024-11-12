import psycopg2

conn = psycopg2.connect(
    dbname="pharmacy",
    user="admin",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS medicines (
    registration_number SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    manufacturing_date DATE NOT NULL,
    shelf_life INTEGER NOT NULL,
    group_type VARCHAR(50),
    price DECIMAL(10, 2),
    prescription_required BOOLEAN
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone VARCHAR(20),
    contact_person VARCHAR(255),
    location VARCHAR(50)
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS supplies (
    supply_id SERIAL PRIMARY KEY,
    supply_date DATE NOT NULL,
    medicine_id INTEGER REFERENCES medicines(registration_number),
    quantity INTEGER NOT NULL,
    supplier_id INTEGER REFERENCES suppliers(supplier_id)
);
""")

conn.commit()

cur.close()
conn.close()
