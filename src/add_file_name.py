import os
import glob
import pandas as pd 


def add_file_name(input_path: str):
    """
    Reads all the data from a specified directory with CSV files, creates a column with the file name
    and saves inplace with the same files

    Args: data_path (str) - the path to the directory containing all the CSV files 

    Returns: 

    """
    
    files_glob = glob.glob(os.path.join(data_path, '*.CSV'))
    
    for f in files_glob:
        df = pd.read_csv(f, encoding="ISO-8859-1", decimal=',',
                        sep=';', error_bad_lines=False,
                        low_memory=False)
        df['file_name'] = int(os.path.splitext(f)[0])
        df.to_csv(f, encoding="ISO-8859-1", sep=';', index=False) # chosen to store with sep=; for easier viewing with Excel
        
    
    return 

if __name__ == '__main__':
    add_file_name('data_test/')