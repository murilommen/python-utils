#!/usr/bin/env python
import os
import glob
import pandas as pd


def append_latest_n(n_files: int, input_path: str):
	"""
	Get the latest files in a specified directory, read them with Pandas and return
	a concatenated unified file

	Args: n_files(int) - number of latest files to consider
		  input_path(str) - folder where the files are contained

	Returns: df_concat(pd.Dataframe) - concatenated DataFrame of latest n files
	"""
	# change the directory to the specified path and create a sorted list
	os.chdir(input_path)
	files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime, reverse=True)

	latest_files = []

	for file in files[:n_files]:
		if file.endswith('.csv') or file.endswith('.CSV'):
			df = pd.read_csv(file, encoding='iso-8859-1', sep=';',  error_bad_lines=False, low_memory=False)
			latest_files.append(df)
		elif file.endswith('.xlsx') or file.endswith('.XLSX'):
			df = pd.read_excel(file)
			latest_files.append(df)
		else:
			print('Files format not currently supported!')

	df_concat = pd.concat(latest_files, axis=0, ignore_index=True)

	return df_concat


def export_df(df: pd.DataFrame, output_path: str, output_type: str):
    """
    Exports a read dataframe into a specified path as CSV or XLSX using pandas
    
    Args: df(pd.DataFrame) - read DataFrame
		  output_path(str) - the directory to where the file should be exported
		  output_type(str) - the type of the desired output format. currently supports 'excel' and 'csv'
    
    Returns: 
    """
    
    if output_type == 'csv':
        df.to_csv(output_path + 'concat_df.csv', index=False)
    elif output_type == 'excel':
        df.to_excel(output_path + 'concat_df.xlsx', index=False, engine='openpyxl')
    else:
        print('Please specify \'csv\' or \'excel\' as the output_type')
    
    return


if __name__ == '__main__':
	input_path = r'data_xlsx/'
	n_files = 5
	output_type = 'excel'
	output_path = r'../output_test/' # navigate one directory above, because of os.chdir()
	df = append_latest_n(n_files, input_path)
	export_df(df, output_path, output_type)
	