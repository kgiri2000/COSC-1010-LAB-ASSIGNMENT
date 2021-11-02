import mi_to_tb 
print ( "Enter Miles" )
miles_str = input()
miles = int(miles_str)
tb = mi_to_tb.mi_to_tb(miles)
print ( "tb = {}".format(tb) )