import pandas as pd
import sys

def csv2md(csv_file_path):   
    data = pd.read_csv(csv_file_path)
    
    markdown_text = data.to_markdown(index=False)
    if markdown_text == None:
        raise Exception(f"Failed to parse data {data}")
    return markdown_text
    

if __name__ == "__main__":
    args = sys.argv
    args_count = len(args)
    if args_count > 3 or args_count <=1:
        print("Usage: python script.py <input_csv_file> <output_markdown_file>")
        sys.exit(1)
    
    csv_path = args[1]
    if args_count == 2:
        md = csv2md(csv_path)
        print(md)

    else:
        md_path = args[2]
        with open(md_path, 'w') as file:
            md = csv2md(csv_path)
            file.write(md)

