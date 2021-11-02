diameter_of_sun = 865370
diameter_of_tb = 2.75/63360
mi_conv = 5878625352016794
km_conv = 9460730472580800
inch_conv = 63360
def mi_to_km(mi):
    conv = 1.60934
    km = mi* conv
    return(km)

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

def km_to_mi(km):
    conv = 1/1.60934
    mi = km * conv
    return(mi)


if __name__ == "__main__":
    n_err = 0
    x = km_to_mi ( 1 )
    if x != 1/1.60934:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( 1/1.60934, x ) )
    x = km_to_mi ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )

    
def ly_to_mi(ly):
    conv = mi_conv
    mi = ly * conv
    return(mi)


if __name__ == "__main__":
    n_err = 0
    x = ly_to_mi ( 1 )
    if x != mi_conv:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( mi_conv, x ) )
    x = ly_to_mi ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )


def ly_to_km (ly):
    conv = km_conv
    km= ly*conv
    return(km)


if __name__ == "__main__":
    n_err = 0
    x = ly_to_km ( 1 )
    if x != km_conv:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( km_conv, x ) )
    x = ly_to_km ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )

def mi_to_tb (mi):
    conv = (diameter_of_tb/diameter_of_sun)
    tb = mi* conv
    return(tb)


if __name__ == "__main__":
    n_err = 0
    x = mi_to_tb ( 1 )
    if x != (diameter_of_tb/diameter_of_sun):
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( (diameter_of_tb/diameter_of_sun), x ) )
    x = mi_to_tb ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )
   

def ly_to_tb (ly):
    conv = (diameter_of_tb/diameter_of_sun)* mi_conv
    tb = ly * conv 
    return(tb)

if __name__ == "__main__":
    n_err = 0
    x = ly_to_tb ( 1 )
    if x != (diameter_of_tb/diameter_of_sun) * mi_conv:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( (diameter_of_tb/diameter_of_sun) * mi_conv, x ) )
    x = ly_to_tb ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )
   

def mi_to_tb_inches (mi):
    conv = (diameter_of_tb/diameter_of_sun)*inch_conv
    tb_inches_mi = mi* conv
    return(tb_inches_mi)

if __name__ == "__main__":
    n_err = 0
    x = mi_to_tb_inches ( 1 )
    if x != (diameter_of_tb/diameter_of_sun) * inch_conv:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( (diameter_of_tb/diameter_of_sun) * inch_conv, x ) )
    x = mi_to_tb_inches ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )
   

def ly_to_tb_inches (ly):
    conv = (diameter_of_tb/diameter_of_sun)* mi_conv* inch_conv
    tb_inches_ly = ly * conv
    return(tb_inches_ly)

if __name__ == "__main__":
    n_err = 0
    x = ly_to_tb_inches ( 1 )
    if x != (diameter_of_tb/diameter_of_sun)* mi_conv* inch_conv:
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format ( (diameter_of_tb/diameter_of_sun)* mi_conv* inch_conv, x ) )
    x = ly_to_tb_inches ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )
   

def au_to_mi(au):
    conv = 92955807.267433
    mi = au * conv
    return(mi)

if __name__ == "__main__":
    n_err = 0
    x = au_to_mi ( 1 )
    if x != 92955807.267433 :
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format (92955807.267433, x ) )
    x = au_to_mi ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )

def au_to_km(au):
    conv = 149597870.691
    km = au * conv
    return(km)

if __name__ == "__main__":
    n_err = 0
    x = au_to_km ( 1 )
    if x != 149597870.691 :
        n_err = n_err + 1
        print ( "Error: Test 1: conversion not working, expected {} got {}".
            format (149597870.691, x ) )
    x = au_to_km ( 0 )
    if x != 0:
        n_err = n_err + 1
        print ( "Error: Test 2: conversion not working, expected {} got {}".
            format ( 0, x ) )
    if n_err == 0 :
        print ( "PASS" )
    else:
        print ( "FAILED" )




