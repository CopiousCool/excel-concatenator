# excel-concatenator
concatenates excel files and produces a 2 new files with the resulting output being an .xlsx file and a .txt file with the successfully concatenated files
The code reads all Excel files in the current working directory, concatenates their data into a single DataFrame, and saves the resulting DataFrame to a new Excel file.

The script first imports the necessary libraries:

os: for accessing files and directories
pandas (pd): for working with data and Excel files
The script then gets the current working directory using the os.getcwd() method and stores it in a variable called current_dir.

A list called df_list is created to hold the DataFrames from each Excel file.

The script then iterates through all the files in the current directory using the os.listdir() method. For each file, it checks if the file extension is '.xlsx' using the file.endswith('.xlsx') method. If the file is an Excel file, the script reads its contents into a DataFrame using the pd.read_excel() method and appends the DataFrame to the df_list.

After all Excel files have been read and their data added to the df_list, the script uses the pd.concat() method to concatenate all the DataFrames in the list into a single DataFrame called result. The ignore_index=True parameter ensures that the concatenated DataFrame has a new index, starting from 0.

Finally, the script uses the to_excel() method to save the concatenated DataFrame to a new Excel file called 'concatenated_file.xlsx'. The index=False parameter tells pandas not to include the index in the output file.
