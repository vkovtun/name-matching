import csv

from tqdm import tqdm


def process_large_csv(input_file, output_file):
    """
    Reads a large CSV file in a streaming fashion and writes a new CSV file
    excluding the fourth column, with a progress bar.

    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file.
    """
    # Get total number of lines for tqdm (optional, for large files this may take time)
    with open(input_file, 'r', encoding='utf-8') as infile:
        total_lines = sum(1 for _ in infile)

    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
            open(output_file, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in tqdm(reader, total=total_lines, desc="Processing CSV", unit="rows"):
            if len(row) >= 5:  # Ensure the row has at least 5 columns
                combined_row = row[:2] + row[4:5]
                trimmed_row = [cell.strip() if isinstance(cell, str) else cell for cell in combined_row]
                writer.writerow(trimmed_row)  # Skip
            else:
                raise ValueError(f"Row {row} has length len(row)")
                #writer.writerow(row)  # Write as-is if it has fewer columns


if __name__ == "__main__":
    input_csv_path = "data/siren_database.csv"  # Change this to your actual input CSV file
    output_csv_path = "data/siren_database_trimmed_2.csv"

    process_large_csv(input_csv_path, output_csv_path)
    print(f"Processed file saved as {output_csv_path}")
