def ly_to_mi ( ly ):
    conv = 5.879e+12
    mi = ly * conv
    return (mi)

# Automated Test
if __name__ == "__main__":
    n_err = 0
    x = ly_to_mi ( 1 )
    if x !=5.879e+12:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( 5.879e+12, x ) )
    x = ly_to_mi ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )
