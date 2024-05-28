import pandas as pd

def split_excel_file(input_file, row_size):
    # Read the large Excel file into chunks
    chunks = pd.read_excel(input_file, chunksize=row_size)
    
    # Iterate through each chunk and save it as a new Excel file
    split_num = 1
    for chunk in chunks:
        output_file = f"{input_file.split('.')[0]}_split{split_num}.xlsx"
        chunk.to_excel(output_file, index=False)
        print(f"Split {split_num}: {output_file} created")
        split_num += 1

# Example usage
if __name__ == "__main__":
    input_file = "large_excel_file.xlsx"  # Replace with your input file name
    row_size = 10000  # Number of rows per split
    split_excel_file(input_file, row_size)
