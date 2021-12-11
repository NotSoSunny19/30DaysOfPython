ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print('min age: ', ages[0])
print('max age: ', ages[len(ages)-1])

# Add the min age and the max age again to the list
MinAndMaxAge = [ages[0],ages[len(ages)-1]]
ages = ages + MinAndMaxAge
print(ages)

# Find the median age (one middle item or two middle items divided by two)
ages.sort()
if(len(ages) % 2 == 1 ):
    MidElement = ages[int(len(ages)/2)]
else:
    MidElement = ages[int((len(ages)-1)/2)]+ages[int((len(ages)+1)/2)]    
median = MidElement/2
print(median)

# Find the average age (sum of all items divided by their number )
average = sum(ages)/len(ages)
print(average)

# Find the range of the ages (max minus min)
ages.sort()
Range = ages[len(ages)-1] - ages[0]
print(Range)

# Compare the value of (min - average) and (max - average), use abs() method
print(abs(ages[len(ages)-1] - average))
print(abs(ages[0] - average))

# Find the middle country(ies) in the countries list
countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Cape Verde",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombi",
    "Comoros",
    "Congo (Brazzaville)",
    "Congo",
    "Costa Rica",
    "Cote d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor Timur)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia, The",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Macedonia",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia and Montenegro",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Swaziland",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]


if(len(countries) % 2 == 1 ):
    MidElement = countries[int(len(countries)/2)]
    print(MidElement)
else:
    MidElement1 = countries[int((len(countries)-1)/2)]
    MidElement2 = countries[int((len(countries)+1)/2)]    
    print(MidElement1)
    print(MidElement2)

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if(len(countries) % 2 == 1 ):
    MidIndex = int(len(countries)/2)
    FirstHalf = countries[:MidIndex]
    SecondHalf = countries[MidIndex:]
    print(FirstHalf)
    print(SecondHalf)
else:
    MidIndex1 = int((len(countries)-1)/2)
    MidIndex2 = int(len(countries)/2)   
    FirstHalf = countries[:MidIndex1]
    SecondHalf = countries[MidIndex2:]
    print('FirstHalf : ',FirstHalf)
    print('SecondHalf : ',SecondHalf)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
NewCountries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
firstCountry, SecondCountry, ThirdCountry, *Scandic = NewCountries 
print(firstCountry,' ', SecondCountry,' ', ThirdCountry)
print(Scandic)