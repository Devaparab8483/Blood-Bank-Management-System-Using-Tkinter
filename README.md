# Blood-Bank-Management-System-Using-Tkinter
# Blood Bank Management System

This is a simple Blood Bank Management System implemented using Python and Tkinter. The application allows you to manage blood donor records and search for donors based on their blood types. It provides a user-friendly graphical interface to add, search, and display donor information.

---

## Features

- **Add Donor**: Add a new donor's details, including their name, age, blood type, and contact information.
- **Search Donors**: Search for donors based on their blood types using checkboxes for multiple selections.
- **Display Results**: View the list of donors matching the selected blood type(s).
- **Validation**: Ensures all fields are filled and validates age and contact information.
- **Clear Fields**: Reset input fields and search results with a single button.
- **Local Data Storage**: Donor information is stored locally in a JSON file for persistence.

---

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

---

## Installation

1. Clone or download the repository to your local machine.

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Ensure Python 3.x is installed on your system.

3. Install any required dependencies (Tkinter is included with most Python installations).

---

## Usage

1. Run the script using Python:

   ```bash
   python blood_bank_management.py
   ```

2. The GUI will open:
   - Enter the donor's name, age, blood type, and contact information to add a donor.
   - Use the checkboxes to select blood types and search for matching donors.
   - View search results in the provided text box.

3. All donor data is saved locally in a file named `blood_donors.json`.

---

## File Structure

- **blood_bank_management.py**: The main Python script for the application.
- **blood_donors.json**: JSON file where donor data is stored. This file is automatically created after adding a donor.

---

## Validations

- **Name**: Cannot be empty.
- **Age**: Must be a number.
- **Blood Type**: Must be selected from the provided options.
- **Contact**: Must be a 10-digit number.

---

## Customization

1. **Adding More Blood Types**:
   - Update the `blood_types` list in the code:
     ```python
     blood_types = ["A+", "B+", "O+", "AB+", "A-", "B-", "O-", "AB-"]
     ```
   - Add these new types to the search section and radio button logic.

2. **Styling**:
   - Modify the colors, fonts, or layout by adjusting parameters in the `Tkinter` widgets.

---

## Limitations

- Data is stored locally in `blood_donors.json` and is not encrypted.
- No advanced search features (e.g., searching by name or contact).
- Application is single-user and does not support concurrent usage.

---

## Screenshots

Include screenshots of the application for better visualization (e.g., add donor form, search results).
![image](https://github.com/user-attachments/assets/dff29b86-0f27-4dc4-8fbb-633711990d13)

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Contributions

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

## Acknowledgements

- Python
- Tkinter
- JSON for local data storage

