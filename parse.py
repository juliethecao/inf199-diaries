import sys
import csv

def parse_csv(file):
    output_rows = []

    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            new_row = []
            for item in row:
                if '06:00-07:00' in item:
                    item = item.replace('06:00-07:00', '06:00 - 07:00')
                if any(char.isdigit() for char in item) or any(char.isalpha() for char in item):
                    new_row.append(item)
                else:
                    parts = item.split(',')
                    new_parts = ['0' for part in parts]
                    new_row.extend(new_parts)
            output_rows.append(new_row)

    return output_rows    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("How to use: python3 parse.py <filename>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "d-" + input_file

    parsed_data = parse_csv(input_file)
    with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(parsed_data)

    print(f"CSV file '{input_file}' has been parsed. Parsed output saved to '{output_file}'.")
