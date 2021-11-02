def mi_to_tb ( mi ):
    conv = (0.0000434/865370)
    tb = mi * conv
    return (tb)

# Automated Test
if __name__ == "__main__":
    n_err = 0
    x = mi_to_tb ( 1 )
    if x != (0.0000434/865370) :
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( (0.0000434/865370), x ) )
    x = mi_to_tb ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )
