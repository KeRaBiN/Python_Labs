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
CREATE OR REPLACE VIEW prescription_medicines AS
SELECT * 
FROM medicines 
WHERE prescription_required = TRUE 
ORDER BY name;
""")


cur.execute("""
CREATE OR REPLACE VIEW medicines_by_group AS
SELECT * 
FROM medicines 
WHERE group_type = 'Painkiller';
""")


cur.execute("""
CREATE OR REPLACE VIEW supply_costs AS
SELECT supply_id, supply_date, quantity, price, quantity * price AS total_cost
FROM supplies
JOIN medicines ON medicines.registration_number = supplies.medicine_id;
""")


cur.execute("""
CREATE OR REPLACE VIEW supplier_payments AS
SELECT supplier_id, SUM(quantity * price) AS total_payment
FROM supplies
JOIN medicines ON medicines.registration_number = supplies.medicine_id
GROUP BY supplier_id;
""")


cur.execute("""
CREATE OR REPLACE VIEW supply_counts AS
SELECT group_type, location, COUNT(*) AS supply_count
FROM supplies
JOIN medicines ON medicines.registration_number = supplies.medicine_id
JOIN suppliers ON suppliers.supplier_id = supplies.supplier_id
GROUP BY group_type, location;
""")


cur.execute("""
CREATE OR REPLACE VIEW last_expiry_dates AS
SELECT name, MAX(manufacturing_date + INTERVAL '1 day' * shelf_life) AS last_expiry_date
FROM medicines
GROUP BY name;
""")


conn.commit()


cur.close()
conn.close()

print("Види створені успішно.")
