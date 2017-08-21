import numpy as np

###########################################################
def random_point():
    return 2*np.random.random()-1

def random_points(number_of_points):
    '''
    This function will create multiple number of points and store them in two lists.
    '''
    x_list=[random_point() for i in range(number_of_points)]
    y_list=[random_point() for i in range(number_of_points)]
    return x_list, y_list
#######################################################################

### This may be a problem if I call this more than once!!!!
def random_line():
    '''
    This function creates a random line function y(x)
    '''
    x1= random_point()
    y1= random_point()
    x2= random_point()
    y2= random_point()
    slope= (y2-y1)/(x2-x1)
    def line(x):
        return slope*(x-x1)+y1
    return line

#####################################################################
def classifier(x,y,line):
    '''
    This function returns the classification of a point from a line
    '''
    if line(x)>y :
        return -1
    else:
        return 1

def point_assigner(x_list, y_list, line):
    '''
    This function returns classification of the points based on the random line    '''
    return [ classifier(x_list[i], y_list[i],line) for i in range(len(x_list)) ] 

###################################################################

