# STEP 0

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("data.sqlite")

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# STEP 1
# Replace None with your code
df_boston = pd.read_sql(
    """SELECT e.firstName, e.lastName FROM employees e JOIN offices o ON e.officeCode = o.officeCode WHERE o.city = 'Boston' """,
    conn,
)

# STEP 2
# Replace None with your code
df_zero_emp = pd.read_sql(
    """ SELECT * FROM offices o LEFT JOIN employees e ON o.officeCode = e.officeCode WHERE e.employeeNumber IS NULL """,
    conn,
)

# STEP 3
# Replace None with your code
df_employee = pd.read_sql(
    """SELECT e.firstName, e.lastName, o.city, o.state  FROM employees e LEFT JOIN offices o ON o.officeCode = e.officeCode ORDER BY e.firstName""",
    conn,
)

# STEP 4
# Replace None with your code
df_contacts = pd.read_sql(
    """SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber FROM customers c LEFT JOIN orders o ON c.customerNumber = o.customerNumber WHERE o.orderNumber IS NULL ORDER BY c.contactLastName""",
    conn,
)

# STEP 5
# Replace None with your code
df_payment = pd.read_sql(
    """SELECT c.contactFirstName, c.contactLastName , p.amount, p.paymentDate FROM customers c LEFT JOIN payments p ON c.customerNumber = p.customerNumber WHERE p.amount IS NOT NULL ORDER BY CAST (p.amount AS DECIMAL) DESC""",
    conn,
)

# STEP 6
# Replace None with your code
df_credit = pd.read_sql(
    """SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) AS customerCount FROM employees e JOIN customers c ON c.salesRepEmployeeNumber = e.employeeNumber GROUP BY e.employeeNumber HAVING AVG(c.creditLimit) > 90000 ORDER BY customerCount DESC LIMIT 4""",
    conn,
)

# print(df_credit)

# STEP 7
# Replace None with your code
df_product_sold = pd.read_sql(
    """ 
SELECT p.productName, COUNT(o.orderNumber) AS numorders, SUM(o.quantityOrdered) AS totalunits FROM products p JOIN orderDetails o ON p.productCode = o.productCode GROUP BY p.productName ORDER BY totalunits DESC
""",
    conn,
)

# STEP 8
# Replace None with your code
df_total_customers = pd.read_sql(
    """SELECT p.productName, p.productCode, COUNT(DISTINCT c.customerNumber) AS numpurchasers FROM products p JOIN orderDetails o ON p.productCode = o.productCode JOIN orders od ON od.orderNumber = o.orderNumber JOIN customers c ON od.customerNumber = c.customerNumber GROUP BY p.productName ORDER BY numpurchasers DESC """,
    conn,
)

# print(df_total_customers)

# STEP 9
# Replace None with your code
df_customers = pd.read_sql(
    """
SELECT o.officeCode, o.city, COUNT(c.customerNumber) AS n_customers FROM offices o JOIN employees e ON o.officeCode = e.officeCode JOIN customers c ON c.salesRepEmployeeNumber = e.employeeNumber GROUP BY o.officeCode
""",
    conn,
)

# STEP 10
# Replace None with your code
df_under_20 = pd.read_sql(
    """
WITH total_products AS (
SELECT p.productName, p.productCode, COUNT(DISTINCT c.customerNumber) AS numpurchasers FROM products p JOIN orderDetails o ON p.productCode = o.productCode JOIN orders od ON od.orderNumber = o.orderNumber JOIN customers c ON od.customerNumber = c.customerNumber GROUP BY p.productCode HAVING numpurchasers <= 19)

SELECT e.employeeNumber, e.firstName, e.lastName, of.city, of.officeCode FROM employees e JOIN officeS of ON of.officeCode = e.officeCode JOIN customers cs ON cs.salesRepEmployeeNumber = e.employeeNumber JOIN orders ord ON ord.customerNumber = cs.customerNumber JOIN orderDetails ords ON ords.orderNumber = ord.orderNumber JOIN total_products tlp ON tlp.productCode = ords.productCode GROUP BY e.employeeNumber ORDER BY e.lastName
""",
    conn,
)

print(df_under_20)

conn.close()
