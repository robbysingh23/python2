# We created a nested dictionaries. Added a key too.

digitalcrafts = {
  'US': {
    'Georgia': {
      'Atlanta': '3442 Piedmont Rd NE #420'
    },
    'Texas': {
      'Houston': '1334 Brittmore Rd #1327'
    }
  }
}
print(digitalcrafts['US']['Texas']['Houston'])

digitalcrafts['US']['South Carolina'] = {
  'Greenville': '123 Sesame Street'
}

print(digitalcrafts)