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
INSERT INTO medicines (name, manufacturing_date, shelf_life, group_type, price, prescription_required)
VALUES
('Aspirin', '2022-01-01', 365, 'Painkiller', 5.50, TRUE),
('Paracetamol', '2023-03-10', 180, 'Painkiller', 3.25, FALSE),
('Vitamin C', '2023-06-15', 365, 'Vitamins', 8.00, FALSE),
('Ibuprofen', '2023-02-01', 365, 'Painkiller', 4.99, TRUE),
('Amoxicillin', '2021-09-01', 365, 'Antibiotic', 7.00, TRUE),
('Cough Syrup', '2023-07-22', 180, 'Antibiotic', 6.75, FALSE),
('Insulin', '2022-11-10', 365, 'Diabetes', 30.00, TRUE),
('Amlodipine', '2022-05-15', 365, 'Cardiovascular', 10.50, FALSE),
('Atenolol', '2022-12-05', 365, 'Cardiovascular', 12.99, TRUE),
('Lisinopril', '2021-11-18', 365, 'Cardiovascular', 15.00, TRUE),
('Folic Acid', '2023-04-11', 365, 'Vitamins', 4.25, FALSE);
""")

cur.execute("""
INSERT INTO suppliers (name, address, phone, contact_person, location)
VALUES
('Pharma Co.', 'Kyiv, Ukraine', '+380123456789', 'Ivanov', 'Ukraine'),
('Med Supplies Ltd.', 'Lviv, Ukraine', '+380987654321', 'Petrov', 'Ukraine'),
('Global Pharma', 'Warsaw, Poland', '+48221234567', 'Kowalski', 'Other Country'),
('EuroMed', 'Berlin, Germany', '+493012345678', 'Schmidt', 'Other Country'),
('Health Partners', 'Budapest, Hungary', '+362012345678', 'Toth', 'Other Country');
""")

cur.execute("""
INSERT INTO supplies (supply_date, medicine_id, quantity, supplier_id)
VALUES
('2023-05-15', 1, 100, 1),
('2023-06-20', 2, 150, 2),
('2023-07-10', 3, 200, 3),
('2023-08-25', 4, 50, 4),
('2023-09-30', 5, 30, 5);
""")

conn.commit()

cur.close()
conn.close()
