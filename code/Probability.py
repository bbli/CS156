def list_classifier(x,y,line):
    '''
    This function takes in two numpy lists and a line function, and produces a list of True False values
    '''
    return line(x)<y
