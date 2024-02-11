import mysql.connector

# Connect to MySQL server
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="test1234*",
            database="client_management"
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

# Insert a new client
def insert_client(connection, name, email, phone, company):
    cursor = connection.cursor()
    query = "INSERT INTO clients (name, email, phone, company) VALUES (%s, %s, %s, %s)"
    data = (name, email, phone, company)
    cursor.execute(query, data)
    connection.commit()
    print("Client added successfully")

# Schedule a meeting for a client
def schedule_meeting(connection, client_id, date_time, agenda):
    cursor = connection.cursor()
    query = "INSERT INTO meetings (client_id, date_time, agenda) VALUES (%s, %s, %s)"
    data = (client_id, date_time, agenda)
    cursor.execute(query, data)
    connection.commit()
    print("Meeting scheduled successfully")

# Retrieve all clients
def get_clients(connection):
    cursor = connection.cursor()
    query = "SELECT * FROM clients"
    cursor.execute(query)
    clients = cursor.fetchall()
    return clients

# Retrieve all meetings for a specific client
def get_meetings(connection, client_id):
    cursor = connection.cursor()
    query = "SELECT * FROM meetings WHERE client_id = %s"
    data = (client_id,)
    cursor.execute(query, data)
    meetings = cursor.fetchall()
    return meetings

#def show_table_info(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"DESCRIBE {table_name}")
    columns = [column[0] for column in cursor.fetchall()]
    print("Columns in table", table_name)
    for column in columns:
        print(column)

# Function to print table information in the terminal
def print_table(connection, table_name):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM " + table_name)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Example usage
def main():
    connection = connect_to_mysql()
    if connection:
        insert_client(connection, "John Doe", "john@example.com", "1234567890", "ABC Inc.")
        insert_client(connection, "Jane Smith", "jane@example.com", "0987654321", "XYZ Corp.")

        schedule_meeting(connection, 1, "2024-01-30 10:00:00", "Discuss project proposal")
        schedule_meeting(connection, 2, "2024-02-05 14:00:00", "Review marketing strategy")

        print("All clients:")
        clients = get_clients(connection)
        for client in clients:
            print(client)

        print("\nMeetings for John Doe:")
        meetings = get_meetings(connection, 1)
        for meeting in meetings:
            print(meeting)
        
        print("CLIENT TABLE IS")
        print_table(connection, 'clients')
        print("MEETING TABLE IS")
        print_table(connection, 'meetings')

        connection.close()

if __name__ == "__main__":
    main()

