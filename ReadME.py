# Smart Banking System – DBMS Project

## 📌 Project Overview

The Smart Banking System is a database-driven application designed to simulate core banking operations using fundamental Database Management System (DBMS) concepts. The system manages customer accounts, transactions, loans, and employee records while ensuring data integrity, security, and consistency.

This project demonstrates practical implementation of relational database design, normalization, SQL queries, and transaction management in a real-world banking scenario.

---

## 🎯 Objectives

- Design a structured relational database for banking operations
- Implement CRUD operations (Create, Read, Update, Delete)
- Maintain data integrity using constraints and keys
- Demonstrate transaction handling and concurrency control
- Apply normalization to eliminate redundancy

---

## 🏗️ Database Design

### Main Entities
- Customer
- Account
- Transaction
- Loan
- Branch
- Employee

### Key Relationships
- A customer can have multiple accounts
- An account belongs to one branch
- Transactions are linked to accounts
- Loans are associated with customers

The database schema follows 3NF (Third Normal Form) to ensure minimal redundancy and logical consistency.

---

## 🔑 Features

- Customer registration and profile management
- Account creation (Savings / Current)
- Deposit and withdrawal operations
- Fund transfer between accounts
- Loan management system
- Transaction history tracking
- Role-based data access (Admin / Staff)

---

## 🛠️ Technologies Used

- MySQL / PostgreSQL (Database)
- SQL (DDL, DML, DCL, TCL)
- [Optional] Java / Python frontend integration
- ER Modeling tools

---

## 📊 DBMS Concepts Implemented

- Primary & Foreign Keys
- Constraints (NOT NULL, UNIQUE, CHECK)
- Joins and Subqueries
- Indexing
- Triggers (if implemented)
- Stored Procedures (if implemented)
- ACID properties
- Transaction control (COMMIT, ROLLBACK)

---

## 🔒 Data Integrity & Security

- Referential integrity maintained through foreign keys
- Controlled transaction handling to prevent inconsistency
- Basic access control implemented for role management

---

## 📈 Future Enhancements

- Online banking interface
- ATM simulation module
- Fraud detection analytics
- API integration
- Encryption for sensitive fields

---

## 📎 Conclusion

The Smart Banking System demonstrates how DBMS principles can be applied to model and manage real-world financial operations efficiently. It highlights the importance of structured schema design, normalization, and transaction management in maintaining a reliable banking database system.