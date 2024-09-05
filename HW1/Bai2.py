def exercise1():
    print ("Exercise 1: Cube's Surface Area")
    edges = float(input("Enter length of edges: "))
    surface_area = 6 * edges**2
    print("Surface area of the cube is: {} m2".format(surface_area))


def exercise2():
    print ("Exercise 2: Five Star Retro Video Store")
    new_videos = int(input("Enter the number of the new videos: "))
    old_videos = int(input("Enter the number of the old videos: "))

    total_videos = new_videos*3 + old_videos*2
    print("Total cost of videos is: {:.2f}$ which is {} new videos and {} old videos".format(total_videos, new_videos, old_videos))

def exercise3():
    print("Exercise 3: Sphere's Detail")
    radius = float(input("Enter the radius of a sphere: "))
    diameter = 2*radius
    circumference = 2*radius*3.14
    surface_area = 4*3.14*radius**2
    volume = 4/3*3.14*radius**3

    print("Sphere(diameter= {:.2f}, circumference= {:.2f}, surface_area= {:.2f}, volume= {:.2f})".format(diameter, circumference, surface_area, volume))

def exercise4():
    print("Exercise 4: Momentum of the object")
    mass = float(input("Enter the mass of the object (kg): "))
    velo = float(input("Enter the velocity of the object (m/s): "))
    momentum = mass*velo
    print("Momentum of the object is: {:.2f} kg.m/s".format(momentum))

def exercise5():
    print("Exercise 5: Kinetic Energy of the object")
    mass = float(input("Enter the mass of the object (kg): "))
    velo = float(input("Enter the velocity of the object (m/s): "))
    kinetic_energy = 0.5*mass*velo**2
    print("Kinetic energy of the object is: {:.2f} J".format(kinetic_energy))

def exercise6():
    print("Exercise 6: Number of minutes in a year (only consider 365 days)")
    n = 60*24*365
    print("Number of minutes in a year: {}".format(n))

def exercise7():
    print("Exercise 7: Light travels")
    number_of_light_year = float(input("Enter the number of light year: "))
    second_per_year = 365*24*60*60 #calculate number of seconds in a year
    light_speed = 3*10**8 # m/s
    distance = number_of_light_year*light_speed*second_per_year
    print("Distance: {:.2e} meters".format(distance))

def exercise8():
    print("Exercise 8: Kilometers to Nautical Miles")
    kilometers = float(input("Enter the number of kilometers: "))
    # Calculate nautical miles using the given approximations
    nautical_miles = kilometers * (1 / 10000) * (90 * 60)
    print("{:.2f} km = {:.2f} nautical miles".format(kilometers, nautical_miles))

def exercise9():
    print ("Exercise 9: Employee's total weekly pay")
    hourly_wage = float(input("Enter the hourly wage ($): "))
    total_regular_hours = float(input("Enter the total regular hours: "))
    total_overtime_hours = float(input("Enter the total overtime hours: "))
    total_weekly_pay = hourly_wage*total_regular_hours + 1.5*hourly_wage*total_overtime_hours
    print("Total weekly pay: {:.2f}$".format(total_weekly_pay))


if __name__ == "__main__":
    # exercise1()
    # exercise2()
    # exercise3()
    # exercise4()
    # exercise5()
    # exercise6()
    # exercise7()
     exercise8()
    # exercise9()

