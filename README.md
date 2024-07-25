# Build a Hotel Booking App in OOP Style with Python

## Description

This project demonstrates how to build a hotel booking application using Object-Oriented Programming (OOP) principles in Python. The app allows users to book hotel rooms, validate and authenticate credit card details, and optionally book spa services. It utilizes data from CSV files to manage hotel and credit card information.

## Process

1. **Data Management**: Load hotel and credit card information from CSV files.
2. **Class Definitions**:
   - **User**: Represents a user of the application (not fully implemented in this example).
   - **Hotel**: Manages hotel booking and availability.
   - **SpaHotel**: Inherits from `Hotel` and includes functionality for booking spa services.
   - **ReservationTicket**: Generates a reservation ticket for hotel bookings.
   - **CreditCard**: Validates credit card details.
   - **SecureCreditCard**: Inherits from `CreditCard` and includes additional authentication features.
   - **SpaTicket**: Generates a reservation ticket for spa bookings.
3. **Booking Process**: The main loop of the application handles hotel booking, credit card validation, and optional spa booking.

## Technology Used

- **Python**: The main programming language used for developing the application.
- **Pandas**: For reading and managing data from CSV files.
- **CSV Files**: Used to store hotel, credit card, and security information.
- **PyCharm IDE**: Used for coding, debugging, and running the application.

## What I Learned from This Project

- **Object-Oriented Programming**: How to use OOP principles to structure a Python application, including class inheritance and method overriding.
- **Data Handling**: Managing and manipulating data using Pandas and CSV files.
- **Authentication and Validation**: Implementing basic credit card validation and authentication mechanisms.
- **Application Logic**: Designing and implementing the core logic for booking hotels and additional services.

## Future Insights

- **User Interface**: Adding a graphical user interface (GUI) to make the application more user-friendly.
- **Database Integration**: Transitioning from CSV files to a database system like SQLite or MySQL for better data management and scalability.
- **Error Handling**: Implementing more robust error handling and validation to ensure application reliability and security.
- **Extended Features**: Adding more features such as room availability checks, booking history, and user account management.

## Project Files

### main.py

The main script that contains the core functionality of the application, including class definitions and booking logic.

### CSV Files

- **hotels.csv**: Contains hotel information including availability.
- **cards.csv**: Contains credit card information for validation.
- **card_security.csv**: Contains additional security information for credit card authentication.
