import psycopg2
from prettytable import PrettyTable


conn = psycopg2.connect(
    dbname="pharmacy",
    user="admin",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


def print_table(query, headers):
    cur.execute(query)
    rows = cur.fetchall()
    table = PrettyTable(headers)
    for row in rows:
        table.add_row(row)
    print(table)


print("\n--- Таблиця: Medicines ---")
print_table("SELECT * FROM medicines", ["registration_number", "name", "manufacturing_date", "shelf_life", "group_type", "price", "prescription_required"])


print("\n--- Таблиця: Suppliers ---")
print_table("SELECT * FROM suppliers", ["supplier_id", "name", "address", "phone", "contact_person", "location"])


print("\n--- Таблиця: Supplies ---")
print_table("SELECT * FROM supplies", ["supply_id", "supply_date", "medicine_id", "quantity", "supplier_id"])


print("\n--- Всі ліки, які відпускаються за рецептом ---")
print_table("SELECT * FROM prescription_medicines;", ["registration_number", "name", "manufacturing_date", "shelf_life", "group_type", "price", "prescription_required"])


group = 'Painkiller'
print(f"\n--- Всі ліки з групи: {group} ---")
print_table(f"SELECT * FROM medicines_by_group WHERE group_type = '{group}';", ["registration_number", "name", "manufacturing_date", "shelf_life", "group_type", "price", "prescription_required"])


print("\n--- Вартість кожної поставки ---")
print_table("SELECT * FROM supply_costs;", ["supply_id", "supply_date", "quantity", "price", "total_cost"])


print("\n--- Загальна сума, яку сплатила аптека кожному постачальнику ---")
print_table("SELECT * FROM supplier_payments;", ["supplier_id", "total_payment"])


print("\n--- Кількість поставок для кожної групи ліків від постачальників з різних локацій ---")
print_table("SELECT * FROM supply_counts;", ["group_type", "location", "supply_count"])


print("\n--- Остання дата придатності для кожної ліки ---")
print_table("SELECT * FROM last_expiry_dates;", ["name", "last_expiry_date"])

cur.close()
conn.close()
