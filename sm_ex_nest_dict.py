ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies','tv']
    }
  ]
}

print(ramit["email"]) #1
print(ramit["interests"][0]) #2
print(ramit['friends'][0]['email']) #3
print(ramit['friends'][1]['interests'][1]) #4