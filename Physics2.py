train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
c = 3*10**8

#conversion tool for fahrenheit to celsius and vise versa
def f_to_c(f_temp, c_temp):
  c_temp = (f_temp - 32) * 5/9  

  return c_temp

def c_to_f(c_temp, f_temp):
  f_temp = c_temp * (9/5) + 32

  return f_temp

def get_force(train_mass, train_acceleration):
  train_force = train_mass * train_acceleration
  
  return train_force

def get_work(train_mass, train_acceleration, train_distance):
  train_work = train_mass * train_acceleration * train_distance
  
  return train_work

def get_energy(bomb_mass, c):
  bomb_energy = bomb_mass * c
  
  return bomb_energy

#defines the values in a function that you created. the function= the equations not the numbers used in the equation.
f100_in_celsius = f_to_c(100, 'c_temp')
c0_in_fahrenheit = c_to_f(0, 'f_temp')
train_force = get_force(22680, 10)
train_work = get_work(22680, 10, 100)
#I defined c as constant which is 3*10**8
bomb_energy = get_energy(1, c)

#print fodder
print(train_force)
print(train_work)
print(bomb_energy)
print(f100_in_celsius)
print(c0_in_fahrenheit)

#print phrases
print("A 1kg bomb supplies" + ' ' + str(bomb_energy) + ' ' + "Joules.")

print("The GE train supplies" + ' ' + str(train_force) + ' ' + "Newtons of force.")

print("The GE train does" + ' ' + str(train_work) + ' ' + "Joules of work over" + ' ' + str(train_distance) + ' ' + "meters." )
