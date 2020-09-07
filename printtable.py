def multtable(start, stop, number):
    """
    Print multiplication table for <number>
    from <start> to including <stop> 
    """
    for i in range(start, stop+1):
        print(f"{i} x {number} = {i*number}")

#if __name__ == '__main__':
#    multtable(1, 4, 7)
    
    
def powertable(power, number):
    '''
    prints power table for number in the power of "power"
    '''
    for i in range(1, number + 1):
        print(i ** power)
if __name__ == '__main__':
    powertable(2,4)
    powertable(3,3)
     