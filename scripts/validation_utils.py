# File: validation_utils.py

import pandas as pd
import os

def read_file(filename):
    """
    Reads a .csv or .xlsx file into a pandas DataFrame based on its extension.
    """
    # Get the file extension
    _, extension = os.path.splitext(filename)
    
    if extension == '.csv':
        return pd.read_csv(filename)
    elif extension == '.xlsx':
        return pd.read_excel(filename)
    else:
        print(f"Unsupported file type: {extension}")
        return None

def check_column_consistency(file_list):
    """
    Checks if all CSV or XLSX files in a list have the same columns.
    """
    if not file_list:
        print("File list is empty.")
        return False

    # Use the helper function to read the first file
    master_df = read_file(file_list[0])
    if master_df is None: return False
    master_columns = master_df.columns.tolist()
    
    # Check the rest of the files
    for filename in file_list[1:]:
        current_df = read_file(filename)
        if current_df is None: return False
        
        if current_df.columns.tolist() != master_columns:
            print(f"❌ Inconsistency Found in '{os.path.basename(filename)}'!")
            return False
            
    print("✅ All files have consistent columns.")
    return True

def consolidate_data(file_list):
    """
    Consolidates a list of CSV or XLSX files into a single DataFrame.
    """
    if not file_list:
        print("❌ File list is empty. Cannot consolidate.")
        return None

    # Use the helper function in a list comprehension
    list_of_dataframes = [read_file(filename) for filename in file_list]
    
    # Filter out any None values in case of unsupported file types
    valid_dataframes = [df for df in list_of_dataframes if df is not None]
    
    if not valid_dataframes:
        print("❌ No valid dataframes to consolidate.")
        return None
    
    consolidated_df = pd.concat(valid_dataframes, ignore_index=True)
    
    print(f"✅ Successfully consolidated {len(valid_dataframes)} files.")
    return consolidated_df