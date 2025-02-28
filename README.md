# South African Phone Number Standardizer

This Python script standardizes South African phone numbers from a spreadsheet (Excel or CSV) into the international format and exports them to a CSV file and a vCard (VCF) file. It handles various phone number formats and ensures consistency for further use.

---

## Features

- **Standardize Phone Numbers**: Converts South African phone numbers to the international format (`+27xxxxxxxxx`).
- **Input Flexibility**: Reads phone numbers from Excel or CSV files.
- **Output Options**:
  - Saves standardized numbers to a CSV file.
  - Generates a vCard (VCF) file for easy contact import into phones or email clients.
- **Error Handling**: Skips invalid or unrecognized phone numbers and logs warnings.

---

## Requirements

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `re`

Install the required libraries using pip:
```
pip install pandas
```

---

## Usage

### Command-Line Interface
Run the script from the command line:
```bash
python script.py input_file.xlsx [encoding]
```

- **`input_file.xlsx`**: Path to the input Excel or CSV file containing phone numbers.
- **`[encoding]`**: (Optional) Specify the file encoding (default: `UTF-8`).

### Input File Format
The input file must contain a column named `Phone number` with the phone numbers to be standardized.

Example input file (`input.xlsx` or `input.csv`):
| Phone number  |
|---------------|
| 0821234567    |

### Output Files
1. **`standardized_numbers.csv`**: Contains the standardized phone numbers.
   Example:
   ```
   phone
   +27821234567
   +27821234567
   +27821234567
   +27821234567
   ```

2. **`contacts.vcf`**: A vCard file with the standardized phone numbers as contacts.
   Example:
   ```
   BEGIN:VCARD
   VERSION:3.0
   N:;Contact1;;;
   FN:Contact1
   TEL;TYPE=CELL:+27821234567
   END:VCARD
   ```

---

## Code Overview

### Functions

1. **`standardize_sa_phone(number)`**:
   - Converts a South African phone number to the international format.
   - Handles various formats (e.g., `0821234567`, ).

2. **`process_spreadsheet(input_file, output_csv, encoding)`**:
   - Reads the input file (Excel or CSV).
   - Standardizes phone numbers and saves them to a CSV file.
   - Logs warnings for invalid numbers.

3. **`save_to_vcard(numbers, filename)`**:
   - Generates a vCard file from the standardized phone numbers.

---

## Example

