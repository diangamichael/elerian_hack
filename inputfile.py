# The solar panel calculator provides detailed information, helping you to find the perfect solar panel size for your house
# Input Values required to calculate
print('Please enter the following details about the location: ')
#: -1.270217          #   location (latitude)
location_lat = input(' Location[latitude] ')
# : 36.769791         #   location (longitute)
location_lon = input(' Location[longitute] ')
# : 6.54                 #   average daily sun hours of the location
sun_hours = input(' Average daily Sun hours')
# : 20                   #   Available roof area, in m^2
roof_area = input(' Available roof area ')
# : 0.9                 #   For further information see https://www.photovoltaik-web.de/photovoltaik/dacheignung/dachausrichtung
efficiency = input(' Efficiency of the solar pannel ')
# : 0.8       #   The proportion of how much energy you want to produce even on days with few hours of sunshine e.g. in the winter
offset_pv_production = input(
    ' Proportion of how much energy you want to produce even on days with few hours of sunshine ')
# : 0.34         #   Peak performance of the (kilo watt peak) of the solar panels
output_kwp_per_m2 = input(
    ' Peak performance of the (kilo watt peak) of the solar panels ')
# : False          #   Electricity mix purchased to date (eco True/False),
eco_electricity = input(
    ' Electricity mix purchased to date (eco Y/N) ').lower()
if eco_electricity == 't':
    eco_electricity = True
else:
    eco_electricity = False
# :  3000  #   energy consumption per year, in kwH
energy_consumption_year = input(' Energy consumption per year, in kwH ')
# : 24.980         #   electricity costs per kwH
energy_cost_kwH = input(' Electricity costs per kwH ')
# : 2000         #   available capital ,
available_capital = input(' Available capital ')
# : 0.15      #   possible loan interest rate.
credit_interest_rate = input(' Possible loan interest rate ')
