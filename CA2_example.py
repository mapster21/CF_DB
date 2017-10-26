car_list = [
        {'make':'Ferrari','colour':'red','mileage':45},
        {'make':'Tesla','colour':'yellow','mileage':245}
]

print car_list

from car import Car
line = 'Petrol,Ferrari,red,45'

petrol_car_list = []
electric_car_list = []
cars_file = open('cars.csv')
for line in cars_file.readlines():
    values = line.strip().split(',')
    if values[0] == 'Petrol':
        petrol_car_list.append(PetrolCar(values[1], values[2], values[3]))
    elif values[0] == 'Electric':
        electric_car_list.append(ElectricCar(values[1], values[2], values[3]))

print petrol_car_list
print electric_car_list

new_car = Car()
new_car = Car('Ferrari', 'red', 45)
new_car = Car(mileage=150)
