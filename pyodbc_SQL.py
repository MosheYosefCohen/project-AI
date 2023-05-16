import pyodbc


# Establish a connection to the SQL Server using Windows Authentication
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-O3SBH8M\SQLEXPRESS01;"
    "Database=NORTHWND;"
    "Trusted_Connection=yes;"
)

# Rest of the code remains the same...


# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute an SQL query
cursor.execute("SELECT Phone FROM Customers WHERE CustomerID = 'BERGS';")

# Fetch the results
results = cursor.fetchall()
for row in results:
    print(*row) # added the * so it will print clean data

# Close the cursor and connection
cursor.close()
conn.close()

'''
table_fields = {
    "Orders": [
        "CustomerID", "EmployeeID", "Freight", "OrderDate", "OrderID",
        "RequiredDate", "ShipAddress", "ShipCity", "ShipCountry", "ShipName",
        "ShippedDate", "ShipPostalCode", "ShipRegion", "ShipVia"
    ],
    "Products": [
        "CategoryID", "Discontinued", "ProductID", "ProductName",
        "QuantityPerUnit", "ReorderLevel", "SupplierID", "UnitPrice",
        "UnitsInStock", "UnitsOnOrder"
    ],
    "Order Details": [
        "Discount", "OrderID", "ProductID", "Quantity", "UnitPrice"
    ],
    "CustomerCustomerDemo": [
        "CustomerID", "CustomerTypeID"
    ],
    "CustomerDemographics": [
        "CustomerDesc", "CustomerTypeID"
    ],
    "Region": [
        "RegionDescription", "RegionID"
    ],
    "Territories": [
        "RegionID", "TerritoryDescription", "TerritoryID"
    ],
    "EmployeeTerritories": [
        "EmployeeID", "TerritoryID"
    ],
    "sysdiagrams": [
        "definition", "diagram_id", "name", "principal_id", "version"
    ],
    "Employees": [
        "Address", "BirthDate", "City", "Country", "EmployeeID",
        "Extension", "FirstName", "HireDate", "HomePhone", "LastName",
        "Notes", "Photo", "PhotoPath", "PostalCode", "Region",
        "ReportsTo", "Title", "TitleOfCourtesy"
    ],
    "Categories": [
        "CategoryID", "CategoryName", "Description", "Picture"
    ],
    "Customers": [
        "Address", "City", "CompanyName", "ContactName", "ContactTitle",
        "Country", "CustomerID", "Fax", "Phone", "PostalCode", "Region"
    ],
    "Shippers": [
        "CompanyName", "Phone", "ShipperID"
    ],
    "Suppliers": [
        "Address", "City", "CompanyName", "ContactName", "ContactTitle",
        "Country", "Fax", "HomePage", "Phone", "PostalCode", "Region",
        "SupplierID"
    ]
}
for x,y in table_fields.items():
    print(x,"^^^^^^",y)
    if ("Country" in y):
        print("Country in y")
'''
