import pandas as pd
import re

# def standardize_sa_phone(number):
#     """Convert various South African phone number formats to the international format."""
#     digits = re.sub(r'\D', '', str(number))
#     original_starts_with_plus27 = str(number).strip().startswith('+27')
#
#     if len(digits) == 10 and digits.startswith('0'):
#         return '+27' + digits[1:]
#     elif len(digits) == 11 and digits.startswith('27'):
#         return '+' + digits
#     elif original_starts_with_plus27 and len(digits) == 11:
#         return '+' + digits
#     elif len(digits) == 9:
#         return '+27' + digits
#     else:
#         return None

def standardize_sa_phone(number):
    """Convert various South African phone number formats to the international format."""
    digits = re.sub(r'\D', '', str(number))
    original_starts_with_plus27 = str(number).strip().startswith('+27')

    if len(digits) == 10 and digits.startswith('0'):
        return '+27' + digits[1:]
    elif len(digits) == 11 and digits.startswith('27'):
        return '+' + digits
    elif original_starts_with_plus27 and len(digits) == 11:
        return '+' + digits
    elif len(digits) == 9:
        return '+27' + digits
    else:
        return None


def process_spreadsheet(input_file, output_csv='standardized_numbers.csv', encoding='UTF-8'):
    """Read CSV with specified encoding and standardize phone numbers."""
    # try:
    # df = pd.read_excel(input_file)
    df = pd.read_excel(input_file, dtype={'Phone number': str})

    # except UnicodeDecodeError:
    #     # Fallback to 'ISO-8859-1' if 'latin-1' fails
    #     df = pd.read_csv(input_file, encoding='ISO-8859-1')

    standardized_numbers = []
    for num in df['Phone number']:
        print(str(num))
        std = standardize_sa_phone(str(num))
        print("standardized: ", std)
        if std:
            standardized_numbers.append(std)
        else:
            print(f"Warning: Could not process number: {num}")

    output_df = pd.DataFrame({'phone': standardized_numbers})
    output_df.to_csv(output_csv, index=False)
    print(f"Standardized numbers saved to {output_csv}")
    return standardized_numbers

def save_to_vcard(numbers, filename="contacts.vcf"):
    """Create a vCard file from standardized numbers."""
    with open(filename, "w") as f:
        for i, number in enumerate(numbers, start=1):
            f.write(f"BEGIN:VCARD\nVERSION:3.0\nN:;Contact{i};;;\nFN:Contact{i}\nTEL;TYPE=CELL:{number}\nEND:VCARD\n")
    print(f"vCard file saved to {filename}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py input_spreadsheet.csv [encoding]")
    else:
        input_file = sys.argv[1]
        encoding = sys.argv[2] if len(sys.argv) > 2 else 'latin-1'  # Default to latin-1
        numbers = process_spreadsheet(input_file, encoding=encoding)
        save_to_vcard(numbers)
