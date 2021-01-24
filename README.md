# codeChallenge

Coding_challenge.py contains a function called getLowTempSprd_Day that consumes a weather data file as input (such as w_data (5).dat). It returns the day with the smallest temperature spread.  Coding_challenge.py also contains another function named getMinGoalDif_Team that consumes a soccer team data file as input (such as soccer.dat) and returns the team with the smallest difference in 'for' and 'against' goals.

In order to run this file you will need to install NumPy (a Python library) using:

pip install numpy

## getLowTempSprd_Day

getLowTempSprd_Day(filename, d_type, skipHeader, skipFooter, useCols, conv_dict, MxT_col, MnT_col, day_col)

Gets the day with the smallest temperature spread. The getLowTempSprd_Day function collects data from a file containing weather data and puts it into a data array. This data array is then used to get the day with the smallest temperature spread. 

filename: name of file to be consumed

d_type: tuple of data types for the resulting array

skipHeader: number of lines to skip at the beginning of the file

skipFooter: number of lines to skip at the end of the file

useCols: tuple of column numbers from the file that indicate what data columns should be stored in the resulting array

conv_dict: dictionary where the keys are column numbers that are mapped to values that are functions. The conv_dict is used to convert the column data using a given function.  
           The converted column data is then stored in the resulting array
           
MxT_col: specifies which column number of the resulting array to store the column of Maximum Temperature data

MnT_col: specifies which column number of the resulting array to store the column of Minimum Temperature data

day_col: specifies which column number of the resulting array to store the column of day number data

## getMinGoalDif_Team

getMinGoalDif_Team(filename, skipHeader, col_to_eval, regex, F_col, A_col, team_col)

Gets the team with the smallest difference in 'for' and 'against' goals. The getMinGoalDif_Team function reads a file with soccer team data. After reading a line, it splits the data by whitespace into a data list, and evaluates whether that data list contains valid data. Evaluation is performed using the helper function is_data_list_valid. The data list is used to find the team with the smallest difference in 'for' and 'against' goals.

filename: name of file to be consumed

skipHeader: number of lines to skip at the beginning of the file

col_to_eval: a column number from the data list to evaluate

regex: a regular expression to evaluate the col_to_eval column in the data list

F_col: the column number in the data list that stores the 'for' goals data 

A_col: the column number in the data list that stores the 'against' goals data

team_col: the column number in the data list that stores the team name data 

## is_data_list_valid 

is_data_list_valid(data_list, col_to_eval, regex)

This a helper function that returns a bool value based on whether a given column of values in a data list matches a given regular expression pattern. 

data_list: a list of data

col_to_eval: the column number in the data_list to evaluate

regex: a regular expression pattern

## Is the way you wrote the second program influenced by writing the first?
Yes, both the first and second programs consume a file and store relevant data in a data structure such as a list or a numpy array. They iterate the data structure while keeping track of the most current smallest difference value found.

Author of coding_challenge.py: Sarah Qadeer
