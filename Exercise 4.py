Cars=100
Space_in_a_car=4.0
Drivers=30
Passengers=90
Cars_not_driven=Cars - Drivers
Cars_driven=Drivers
Carpool_capacity=Cars_driven - Space_in_a_car
Average_passengers_per_car=Passengers/Cars_driven


print'There are',Cars,'cars available.'
print'There are',Drivers,'drivers available.'
print'There will be',Cars_not_driven,'empty cars today.'
print'We can transport',Carpool_capacity,'people today.'
print'We have',Passengers,'to carpool today'
print'We need to put about', Average_passengers_per_car,'in each car'