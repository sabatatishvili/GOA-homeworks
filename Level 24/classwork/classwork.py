#def digitize(n):
    #return [int(d) for d in str(n)][::-1]
#-------------------------------------------------
#def to_alternating_case(string):
    #return string.swapcase()
#--------------------------------------------------
#def abbrev_name(name):
    #first, second = name.split()
    #return f"{first[0].upper()}.{second[0].upper()}"
#------------------------------------------------------
#def rps(p1, p2):
    #if p1 == p2:
        #return "Draw!"
    #elif (p1 == 'rock' and p2 == 'scissors') or \
         #(p1 == 'scissors' and p2 == 'paper') or \
         #(p1 == 'paper' and p2 == 'rock'):
        #return "Player 1 won!"
    #else:
        #return "Player 2 won!"
#-----------------------------------------------------------
#def feast(beast, dish):
    #return beast[0] == dish[0] and beast[-1] == dish[-1]