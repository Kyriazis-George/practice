# users = {
#     'George':{
#         'first':'George',
#         'last':'Kyriazis',
#         'location':'Leeds',
#         'job':'musician',
#         },

#     'Zoi':{
#         'first':'Zoi',
#         'last':'Antonopoulou',
#         'location':'Leeds',
#         'job':'disability advisor'
#         }}

# for key,value in users.items():
#     print(f"\nUsername:{key}")
#     full_name = f"{value['first']} {value['last']}"
#     location = value['location']
#     job = value['job']

#     print(f"\tFull name: {full_name.title()}")
#     print(f"location {location.title()}")
#     print(f"\njob: {job.upper()}")

# pets = {'Nelson': {'name':'Nelson',
#                    'kind': 'dog',
#                    'owner':'John',
#                    },

#         'Kookik':{'name':'Kookik',
#                   'kind':'parrot',
#                   'owner':'George',
#         },

#         'Max':   {'name':'Max',
#                 'kind':'cat',
#                 'owner':'Bill',
#         }}
       
# for key, value in pets.items():
#     print(f"\nName:{key}")
#     pet = f"{value['name']} {value['kind']}"
#     owner = f"{value['owner']}"

#     print(f"\t My pet is :{pet.title()}")    
#     print(f"\t the owners name is: {owner}")       


# favorite_places = {'George':['Xanthi','Thessaloniki','Maronia'],
#                    'Zoi':['Pirgos','Athens','Leeds'],
#                    'Anastasia':['Antiphilipoi','Vafeika','Komotini']}

# for name, places in favorite_places.items():
#     print(f"\n{name.title()}'s favorite places are:")
# for place in places:
#     print(f"\n{place.title()}")


# favorite_number = {'George':[1, 5],
#                    'Zoi':[4, 13],
#                    'Mike':[8,9],
#                    'John':[7,22]
# }

# for name,numbers in favorite_number.items():
#     print(f"\n{name.title()}'favorite numbers are:")
# for number in numbers:
#     print(f"\n{number}")
   
# cities = {'Thessaloniki':{'Country':'Greece',
#                           'Population':1000000,
#                           'Fact':'Sea-Side'},
                          
#                           'Leeds':{'Country':'England',
#                                    'Population':800000,
#                                    'Fact':'River-Side'},

#                           'Xanth':{'Country':'Greece',
#                                    'Population':55000,
#                                    'Fact':'Mountain-Side'},         
#                           }

# for name, city_info in cities.items():
#     print(f"\n Name:{name}")
#     full_details = f"Is a town in {city_info['Country']} with the population of {city_info['Population']} people"
#     fun_fact = f"Is a town with nice {city_info['Fact']}"


#     print(f"\tFull details: {full_details}")
#     print(f"\tfun_fact:{fun_fact}")

# users = {
#     'George':{
#         'first':'George',
#         'last':'Kyriazis',
#         'location': {'city':'Leeds',
#                      'area':'Beeston'},
#         'job':'musician',
#         },

#     'Zoi':{
#         'first':'Zoi',
#         'last':'Antonopoulou',
#         'location':{'city':'Leeds',
#                     'area':'Hunslet'},
#         'job':'disability advisor'
#         }}

# for key,value in users.items():
#     print(f"\nUsername:{key}")
#     full_name = f"{value['first']} {value['last']}"
#     job = value['job']
#     full_location = f"{value['location']['city']} - {value['location']['area']}"
 
#     print(f"\tFull name: {full_name.title()}")
#     print(f"location : {full_location}")
#     print(f"\njob: {job.upper()}")


# users = {
#     'George':{
#         'first':'George',
#         'last':'Kyriazis',
#         'location': {'city':'Leeds',
#                      'area':{'name':'Beeston',
#                                 'post-code':'ls12',
#                                  'adress':'Dewsbury Road'}},
#         'job':{'title':'musician',
#                'employer':'self-employed'}
#         },

#     'Zoi': {
#         'first':'Zoi',
#         'last':'Antonopoulou',
#         'location': {'city':'Leeds',
#                     'area':{'name':'Hunslet',
#                             'post-code':'ls12',
#                             'adress': 'Hunslet Road'}},
                        
#         'job':{'title': 'disability advisor',
#                'employer' : 'Arden University'}

#         }}

# for key,value in users.items():
#     print(f"\nUsername:{key}")
#     full_name = f"{value['first']} {value['last']}"
#     job = (f"\t{value['job']['title']}"
#            f"\t{value['job']['employer']}")
#     full_location = (f"\t{value['location']['city']} -"
#                      f"\t{value['location']['area']['name']}"
#                      f"\t{value['location']['area']['post-code']}"
#                      f"\t{value['location']['area']['adress']}"
#                     )
 
#     print(f"\tFull name: {full_name.title()}")
#     print(f"location : {full_location}")
#     print(f"\njob: {job.upper()}")