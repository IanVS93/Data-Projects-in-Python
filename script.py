# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def damage_convert(damages):
  conversion = {"M": 1000000,
              "B": 1000000000}
  updated_damages = list()
  for damage in damages:
    if damage == "Damages not recorded":
       updated_damages.append(damage)
    if damage.find('M') != -1:
       updated_damages.append(float(damage[0:damage.find('M')])*conversion["M"])
    if damage.find('B') != -1:
     updated_damages.append(float(damage[0:damage.find('B')])*conversion["B"])
  return  updated_damages
# test function by updating damages
updated_damages = damage_convert(damages)
# 2 
# Create a Table
def hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
  hurricanes = {}
  num_hurricanes = len(names)
  for index in range(num_hurricanes):
    hurricanes[names[index]] = {"Name": names[index], "Month": months[index], "Year": years[index], "Max Sustained Wind": max_sustained_winds[index], "Areas Affected": areas_affected[index], "Damage": updated_damages[index], "Deaths": deaths[index]}
  return hurricanes
# Create and view the hurricanes dictionary
hurricanes = hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
# 3
# Organizing by Year
def year_dictionary(hurricanes):
  year_hurricane = {}
  for index in year_hurricane:
    current_year = hurricanes[index]["Year"]
    current_cane = hurricanes[index]
    if current_year in year_hurricane:
      year_hurricane[current_year].append(current_cane)
    else:
      year_hurricane[current_year] = [current_cane]
  return  year_hurricane
# create a new dictionary of hurricanes with year and key
year_dictionary = year_dictionary(hurricanes)
# 4
# Counting Damaged Areas
def count_damaged_areas(hurricanes):
  area_count = {}
  for index in hurricanes:
    for area in hurricanes[index]["Areas Affected"]:
      if area in area_count:
        area_count[area] += 1
      else:
        area_count[area] = 1
  return area_count
# create dictionary of areas to store the number of hurricanes involved in
damaged_areas_count = count_damaged_areas(hurricanes)
# 5 
# Calculating Maximum Hurricane Count
def biggest_affected_area(hurricanes):
  max_area = ''
  max_area_count = 0
  for area in damaged_areas_count:
    if damaged_areas_count[area] > max_area_count:
      max_area = area
      max_area_count = damaged_areas_count[area]
  return max_area, max_area_count
# find most frequently affected area and the number of hurricanes involved in
max_area, max_area_count = biggest_affected_area(count_damaged_areas)
#print(max_area,max_area_count)
# 6
# Calculating the Deadliest Hurricane
def deadliest_hurricane(hurricanes):
  max_mortality_hurricane = ''
  max_mortality = 0
  for index in hurricanes:
    if hurricanes[index]["Deaths"] > max_mortality:
      max_mortality_hurricane = index
      max_mortality = hurricanes[index]["Deaths"]
  return  max_mortality_hurricane, max_mortality
# find highest mortality hurricane and the number of deaths
max_mortality_hurricane, max_mortality = deadliest_hurricane(hurricanes)
#print(max_mortality_hurricane, max_mortality)
# 7
# Rating Hurricanes by Mortality
def mortality_rating(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
  mortality = {}
  for index in hurricanes.keys():
    rate = 0
    num_deaths = hurricanes[index]["Deaths"]
    if num_deaths == 0:
      mortality[index] = 0
    elif num_deaths < 100:
      mortality[index] = 1
    elif num_deaths < 500:
      mortality[index] = 2
    elif num_deaths < 1000:
      mortality[index] = 3
    elif num_deaths < 10000:
      mortality[index] = 4
    else:
      mortality[hurricane] = 5
    return mortality
# categorize hurricanes in new dictionary with mortality severity as key
mortality_rates = mortality_rating(hurricanes)
#print(mortality_rates)
# 8 Calculating Hurricane Maximum Damage
def greatest_damage(hurricanes):
  max_damage_cane = ''
  max_damage = 0
  for index in hurricanes:
    if hurricanes[index]["Damage"] == 'Damages not recorded':
      pass
    elif hurricanes[index]['Damage'] > max_damage:
      max_damage_cane = hurricanes[index]['Name']
      max_damage = hurricanes[index]['Damage']
  return max_damage_cane, max_damage
# find highest damage inducing hurricane and its total cost
max_damage_cane, max_damage = greatest_damage(hurricanes)
#print(max_damage_cane, max_damage)
# 9
# Rating Hurricanes by Damage
def damage_rating(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for index in hurricanes:
    type_damage = hurricanes[index]['Damage']
    if type_damage == 'Damages not recorded':
      hurricanes_by_damage[0].append(hurricanes[index])
    elif type_damage == damage_scale[0]:
      hurricanes_by_damage[0].append(hurricanes[index])
    elif type_damage > damage_scale[0] and type_damage <= damage_scale[1]:
      hurricanes_by_damage[1].append(hurricanes[index])
    elif type_damage > damage_scale[1] and type_damage <= damage_scale[2]:
      hurricanes_by_damage[2].append(hurricanes[index])
    elif type_damage > damage_scale[2] and type_damage <= damage_scale[3]:
      hurricanes_by_damage[3].append(hurricanes[index])
    elif type_damage > damage_scale[3] and type_damage <= damage_scale[4]:
      hurricanes_by_damage[4].append(hurricanes[index])
    else:
      hurricanes_by_damage[5].append(hurricanes[index])
  return hurricanes_by_damage
#print(damage_scale)
hurricanes_by_damage = damage_rating(hurricanes)
print(hurricanes_by_damage[3])
# categorize hurricanes in new dictionary with damage severity as key
