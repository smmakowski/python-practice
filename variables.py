# print out how far light travels in centimeters in one nanosecond

# base information

speed_of_light_meters_second = 299792458
centimeters_in_meter = 100
nanoseconds_in_second = 1000000000.0

# calculation variables
centimeters_in_second = speed_of_light_meters_second * centimeters_in_meter

print('Light travels ' + str(centimeters_in_second / nanoseconds_in_second) + ' centimeters in 1 nanosecond.')

# print out distance light travels in one processor cycle of 2.7GHzprocessor

speed_of_light = 299792458.0 # meters per second
cycles_per_second = 2700000000.0 # cycles for 2.7GHz

print('Light travels ' + str(speed_of_light / cycles_per_second) + ' meters in one processor cycle.')

# variable reassignment

a = 10
a = a + 1
a = a * 10

print(a) # a will be 20

# calculate in days in 35 years
total_years = 35
days_in_year = 365

print(total_years * days_in_year)

