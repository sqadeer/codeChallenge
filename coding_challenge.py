#*******************************************************************
#  Code Challenge                                                   
#*******************************************************************
import math
import numpy as np
import re

'''
Gets the day with the smallest temperature spread. The getLowTempSprd_Day
function collects data from a file containing weather data and puts it into
a data array. This data array is then used to get the day with the smallest
temperature spread. 

filename: name of file to be consumed
d_type: tuple of data types for the resulting array
skipHeader: number of lines to skip at the beginning of the file
skipFooter: number of lines to skip at the end of the file
useCols: tuple of column numbers from the file that indicate what data columns
         should be stored in the resulting array
conv_dict: dictionary where the keys are column numbers that are mapped to values that
           are functions. The conv_dict is used to convert the column data using a given function. The converted column
           data is then stored in the resulting array
MxT_col: specifies which column number of the resulting array to store the column of Maximum Temperature data
MnT_col: specifies which column number of the resulting array to store the column of Minimum Temperature data
day_col: specifies which column number of the resulting array to store the column of day number data
'''
def getLowTempSprd_Day(filename, d_type, skipHeader, skipFooter, useCols, conv_dict, MxT_col, MnT_col, day_col):
    
    data_array = np.genfromtxt(filename,dtype= d_type,skip_header= skipHeader, skip_footer= skipFooter, 
                                    usecols= useCols, converters= conv_dict)
    min_spread = math.inf
    day = 0
    for row in data_array:
        spread = row[MxT_col] - row[MnT_col]
        if spread < min_spread:
            min_spread= spread
            day = row[day_col]
    return day   


'''
Gets the team with the smallest difference in 'for' and 'against' goals. The
getMinGoalDif_Team function reads a file with soccer team data. After reading a 
line, it splits the data by whitespace into a data list, and evaluates whether that data list
contains valid data. Evaluation is performed using the helper function is_data_list_valid.
The data list is used to find the team with the smallest difference in 'for' and 'against' goals.

filename: name of file to be consumed
skipHeader: number of lines to skip at the beginning of the file
col_to_eval: a column number from the data list to evaluate
regex: a regular expression to evaluate the col_to_eval column in the data list
F_col: the column number in the data list that stores the 'for' goals data 
A_col: the column number in the data list that stores the 'against' goals data
team_col: the column number in the data list that stores the team name data  
'''
def getMinGoalDif_Team(filename, skipHeader, col_to_eval, regex, F_col, A_col, team_col):
    min_goal_dif = math.inf
    team = ''
    with open(filename, 'r') as f:
        # skipping skipHeader number of lines in the beginning of the file
        for i in range(0, skipHeader):
            next(f)
            
        for line in f:
            data_list = line.split()
            if len(data_list) > 0 and is_data_list_valid(data_list, col_to_eval, regex): 
                goal_dif = abs(int(data_list[F_col]) - int(data_list[A_col]))
                if goal_dif < min_goal_dif:
                    min_goal_dif = goal_dif
                    team = data_list[team_col]
    return team       



'''
Returns a bool value based on whether a given column of values in a data list matches
a given regular expression pattern. 

data_list: a list of data
col_to_eval: the column number in the data_list to evaluate
regex: a regular expression pattern
'''   
def is_data_list_valid(data_list, col_to_eval, regex):
    pattern = re.compile(regex)
    if pattern.match(data_list[col_to_eval]) == None : return False
    return True

if __name__ == '__main__':
    lts_file = 'w_data (5).dat'
    lts_d_type = (int, int, int)
    lts_skipHeader = 5
    lts_skipFooter = 2
    lts_useCols = (0,1,2)
    # remove_star is a conversion func that takes in a bytes string.
    # Occurences of '*' are removed from the bytes string.
    # Finally, it converts the string into a float.
    remove_star = lambda x: float(x.replace(b'*', b''))  
    lts_conv_dict = {1: remove_star, 2: remove_star}
    MxT_col = 1
    MnT_col = 2
    day_col = 0

    print('Day Number with the Smallest Temperature Spread: ')
    print(getLowTempSprd_Day(lts_file, lts_d_type, lts_skipHeader, lts_skipFooter, lts_useCols, lts_conv_dict, MxT_col, MnT_col, day_col))
    print()

    mgd_file = 'soccer.dat'
    mgd_skipHeader = 3
    col_to_eval = 0
    regex = r'^[0-9]*.$'
    F_col = 6
    A_col = 8
    team_col = 1
    
    print("Team with Smallest Difference in 'for' and 'against' goals: ")
    print(getMinGoalDif_Team(mgd_file, mgd_skipHeader, col_to_eval, regex , F_col, A_col, team_col))
    print()
    print('Is the way you wrote the second program influenced by writing the first?')
    print('Yes, both the first and second programs consume a file and store relevant data in a data structure')
    print('such as a list or a numpy array. They iterate the data structure while keeping track of the most' )
    print('current smallest difference value found.')      
          