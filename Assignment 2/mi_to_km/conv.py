def mi_to_km ( mi ):
    conv = 1.60934
    km = mi * conv
    return (km)

# Automated Test
if __name__ == "__main__":
    n_err = 0
    x = mi_to_km ( 1 )
    if x != 1.60934:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( 1.60934, x ) )
    x = mi_to_km ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )
