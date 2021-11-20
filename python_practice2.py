counties = ["arapahoe", "denver", "jefferson"]

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the lsit of counties.")
    for county in counties:
        print(county)
    for i in range(len(counties)):
        print(counties[i])
counties_dict= {"arapahoe": 422829, "denver": 463353, "jefferson": 432438}
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
voting_data= [{"county":"Arapahoe", "registered_voters": 422829},
    {"county":"Denver", "registered_voters": 463353},
    {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     print(county_dict) 
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for county, voters in county_dict.items():
#     print(f"{county} county has {voters} registered voters.")
for key in counties_dict:
    print(f"{key} county has {counties_dict[key]:,} number of registered voters.")
    