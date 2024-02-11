-- Create database
CREATE DATABASE client_management;

-- Use the database
USE client_management;

-- Create table for clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    company VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for meetings
CREATE TABLE meetings (
    meeting_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    date_time DATETIME NOT NULL,
    agenda TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

show databases;
