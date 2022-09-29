# In order to Run this file you need to install the module suntime (pip3 install suntime) and datetime
# Importing required models

from elarian import Elarian
from functions import *
from sms import *
import matplotlib.pyplot as plt  # needed if you want to plot the comparison of costs
import asyncio
#########################################################################################
# Reading input file and creating a dictionary with the required input values ###########
#########################################################################################

# name = "input.txt"
# value_inputs = open(name)
# list_input_values = {}
# for line in value_inputs:
#     if line[0] == "#":  # ignoring Comments from file
#         continue
#     words = line.split()
#     if len(words) < 1:  # ignoring empty lines
#         continue
#     input_variable = words[0]
#     input_value = words[1]
#     list_input_values[input_variable] = input_value


# Input Values required to calculate
print('Please enter the following details about the location: ')
#: -1.270217          #   location (latitude)
location_lat = input(' Location[latitude] ')
# : 36.769791         #   location (longitute)
location_lon= input(' Location[longitute] ')
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
co2_per_kwH_in_KG = 0.401  # source https://www.co2online.de/energie-sparen/strom-sparen/strom-sparen-stromspartipps/was-ist-echter-oekostrom/
oeko_co2_per_kwH_proportion = 0.1  # source: https://www.co2online.de/energie-sparen/strom-sparen/strom-sparen-stromspartipps/was-ist-echter-oekostrom/
co2_per_kwH_SOLAR_in_KG = 0.05
invest_1kWp_solar = 1350  # Euro source: https://www.rechnerphotovoltaik.de/rechner/amortisationszeit

#########################################################################################
# Converting required input values of the dictionary into floating points ###############
# and assign them to variables #########################################################
#########################################################################################

latitude_val = convert_to_float(location_lat)
longitude_val = convert_to_float(location_lon)
sun_hour_average = convert_to_float(sun_hours)
roof_area = convert_to_float(roof_area)
efficiency = convert_to_float(efficiency)
offset_pv_production = convert_to_float(offset_pv_production)
yearly_energy_consumption = convert_to_float(energy_consumption_year)
output_per_m2 = convert_to_float(output_kwp_per_m2)
energy_costs = convert_to_float(energy_cost_kwH)
eco_energy = eco_electricity
available_capital = convert_to_float(available_capital)
credit_interest_rate = convert_to_float(credit_interest_rate)
# The solar panel calculator provides detailed information, helping you to find the perfect solar panel size for your house
##################################################################################
# Creating a list based on the location and the average daily sun hours (year) ###
##################################################################################
LST__date_sun_hours_clear_sky = daily_sun_hours_clear_sky_lst_one_year(2022, latitude_val, longitude_val)
LST_sun_hours = correcting_sun_hour_clear_sky__observed_average(sun_hour_average, LST__date_sun_hours_clear_sky)

##################################################################################
# Calculating wanted key figures #################################################
##################################################################################


output_PV_needed_in_KWh = max_kwh_needed_output(yearly_energy_consumption, LST_sun_hours, offset_pv_production,
                                                efficiency)
needed_pv_area = needed_solar_area_size(output_PV_needed_in_KWh, output_per_m2)
enough_roof_area_available = enough_roof_area(roof_area, needed_pv_area)
investment_pv_area = needed_pv_area * invest_1kWp_solar
if investment_pv_area > available_capital:
    credit_need = investment_pv_area - available_capital
else:
    credit_need = 0.0

energy_savings = energy_savings_kw_h(yearly_energy_consumption, LST_sun_hours, output_PV_needed_in_KWh, efficiency)
costs_without_solar = yearly_energy_consumption * energy_costs
co2_production = co2_production_no_solar(yearly_energy_consumption, co2_per_kwH_in_KG, eco_energy)
co2_savings_with_solar = co2_savings_sol(co2_production, yearly_energy_consumption, energy_savings, co2_per_kwH_SOLAR_in_KG)
costs_savings = energy_savings * energy_costs
pay_back_years_credit = years_to_credit_free(credit_need, credit_interest_rate, costs_savings)
armortization_years, sum_interest_credit, LST_compare_NO_solar_costs, LST_compare_solar_costs = years_to_armortization(
    investment_pv_area, credit_need, credit_interest_rate, costs_without_solar, costs_savings)


# Printing the key figures 

print(
    f"\nYou consumed last year {yearly_energy_consumption:.0f} kwH, with the price of {energy_costs:.3f}KSH per kwH. \nYou paid {costs_without_solar:.0f} KSH.")
print(f"Thus you produced {co2_production:.0f} kg co2.")
print(f"\nYou want to produce {offset_pv_production * 100:.0f}% of energy consumption even on regular cloudy days.")
if not enough_roof_area_available:
    print("To do so you do not have enough roof area.\n")
    y = print("To do so you do not have enough roof area.\n")
    # Initialize a service e.g. SMS
    class sms():

        sms = africastalking.SMS 
  
        def sending(self):
            # Set the numbers in international format
            recipients = ["+254735000014"]
            # Set your message
            message = "To do so you do not have enough roof area.\n";
            # Set your shortCode or senderId
            sender = "13610"

            try:
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Sam, we have a problem: {e}')
    sms().sending()

if enough_roof_area_available:
    print("To do so you have enough roof area: NICE!")
    print(f"You need to install {needed_pv_area:.2f}m^2 and you need to invest {investment_pv_area:.0f} KSH in order to achieve your solar production goal.")
    print(f"With the {needed_pv_area:.2f} m2 area of solar panels you can produce {energy_savings:.1f} kwH, \nand save yearly {costs_savings:.0f} KSH and  {co2_savings_with_solar:.0f} kg CO2. \nAfter {armortization_years} years you save money compared to not having solar panels.")
    if credit_need > 0:
        print(
            f"You need to borrow {credit_need:.0f} KSH , based on your interest rate of {credit_interest_rate * 100:.1f} % you need to pay {sum_interest_credit:.0f} KSH interest, "
            f"\nand if you pay back the yearly cost savings of installing solar panels you can pay back the credit in {pay_back_years_credit} years ")
    print("\n")
    # Initialize a service e.g. SMS
    class sms():

        sms = africastalking.SMS 
  
        def sending(self):
            # Set the numbers in international format
            recipients = ["+254735000014"]
            # Set your message
            message = "Hello Esteemed customer, You have enough roof area and the qualification to implement the solar solution. A detailed Quote will be sent to your inbox shortly.Have a Lovely day : NICE!.\n";
            # Set your shortCode or senderId
            sender = "13610"

            try:
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print (f'Mike, we have a problem: {e}')
    sms().sending()
##################################################################################
# Plotting the costs of solar energy vs no solar energy ##########################
##################################################################################

plt.figure(figsize=(5, 3), constrained_layout=True)
plt.plot(LST_compare_solar_costs, label="Solar_costs")
plt.plot(LST_compare_NO_solar_costs, label="NO_Solar_costs")
plt.xlabel('Years')
plt.ylabel('Costs in KSH')
plt.title("Comparison Solar Costs vs. No Solar Costs")
plt.legend()
plt.savefig('plot_solarcosts_vs_nosolarcosts.svg', dpi=350)



