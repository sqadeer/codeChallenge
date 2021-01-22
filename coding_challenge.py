#*******************************************************************
#  Code Challenge                                                   
#*******************************************************************
import math

'''
Gets the day with the smallest temperature spread.
'''
def getLowTempSprd_Day():
    min_spread = math.inf
    day = ''
    with open('w_data (5).dat', 'r') as f:
        for line in f:
            data = line.split()
            if len(data) > 0 and data[0].isnumeric(): 
                spread = int(data[1].replace('*', '')) - int(data[2].replace('*','')) # removes "*" from MxT and MnT
                if spread < min_spread:
                    min_spread = spread
                    day = data[0]   
    return day


'''
Gets the team with the smallest difference in 'for'
and 'against' goals.
'''
def getMinGoalDif_Team():
    min_goal_dif = math.inf
    team = ''
    with open('soccer.dat', 'r') as f:
        for line in f:
            data = line.split()
            if len(data) > 0 and data[0].replace('.','').isnumeric():  # removes "." from the row number
               goal_dif = abs(int(data[6]) - int(data[8]))
               if goal_dif < min_goal_dif:
                   min_goal_dif = goal_dif
                   team = data[1]
    return team       

if __name__ == '__main__':
    print('Day Number with the Smallest Temperature Spread: ' + getLowTempSprd_Day())
    print("Team with Smallest Difference in 'for' and 'against' goals: " + getMinGoalDif_Team())
    print()
    print('Is the way you wrote the second program influenced by writing the first?')
    print('Yes, both the first and second programs iterate a file while storing the most current smallest difference value found.')