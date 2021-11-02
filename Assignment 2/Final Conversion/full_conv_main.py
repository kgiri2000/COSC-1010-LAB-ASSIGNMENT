import full_conv
print("Press 1 for miles to kilometers: ")
print("Press 2 for kilometer to miles: ")
print("Press 3 for light year to miles: ")
print("Press 4 for light year to kilometers: ")
print("Press 5 for miles to tennis unit(miles): ")
print("Press 6 for light year to tennis unit(miles):")
print("Press 7 for miles to tennis unit(inches):")
print("Press 8 for light year to tennis unit(inches)")
print("Press 9 for AU to miles conversion:")
print("Press 10 for AU to km Conversion:")
num_str = input()
num= int(num_str)

if num==1:
    print("Enter Value in Miles:")
    mi_str = input()
    mi = float(mi_str)
    km = full_conv.mi_to_km(mi)
    print("Resultant Kilometers: {}".format(km))

elif num==2:
    print("Enter Value in Kilometers:")
    km_str= input()
    km = float(km_str)
    mi = full_conv.km_to_mi(km)
    print("Resultant Miles = {}".format(mi))

elif num == 3:
    print( "Enter Value in Light year" )
    ly_str=input()
    ly = float(ly_str)
    mi = full_conv.ly_to_mi(ly)
    print("Resultant Miles : {}".format(mi))

elif num ==4:
    print("Enter Value in Light Year:")
    ly_str = input()
    ly = float(ly_str)
    km = full_conv.ly_to_km(ly)
    print("Resultant Kilometers: {}".format(km))

elif num ==5 :
    print("Enter the value in Miles:")
    mi_str= input()
    mi = float(mi_str)
    tb= full_conv.mi_to_tb(mi)
    print("resultant Tb unit(miles) is{} :".format(tb))

elif num==6:
    print("Enter the value in light year:")
    ly_str = input()
    ly = float(ly_str)
    tb = full_conv.ly_to_tb(ly)
    print("Resultant Tb unit(miles) is{} :".format(tb))

elif num==7:
    print("Enter the value in Miles:")
    mi_str= input()
    mi = float(mi_str)
    tb_inches_mi= full_conv.mi_to_tb_inches(mi)
    print("resultant Tb unit(inches) is{} :".format(tb_inches_mi))

elif num==8:
    print("Enter the value in light year:")
    ly_str = input()
    ly = float(ly_str)
    tb_inches_ly = full_conv.ly_to_tb_inches(ly)
    print("Resultant Tb unit(inches) is{} :".format(tb_inches_ly))

elif num ==9:
    print("Enter your value in AU:")
    au_str = input()
    au = float(au_str)
    mi = full_conv.au_to_mi(au)
    print("Resultant AU in miles  : {}".format(mi))

elif num==10:
    print("Enter the value in AU:")
    au_str = input()
    au = float(au_str)
    km = full_conv.au_to_km(au)
    print("Resultant value in km: {}".format(km))
     


else :
    print("Please enter valid number")