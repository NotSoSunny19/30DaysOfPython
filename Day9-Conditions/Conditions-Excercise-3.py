#     Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if 'skills' in person.keys():
    SkillsOfStudent = person['skills']
    print(SkillsOfStudent)
    Num_of_Skills = len(SkillsOfStudent)
    print(Num_of_Skills)
    if (Num_of_Skills % 2) == 0 :
        print(str(SkillsOfStudent[int(Num_of_Skills/2)]))
    else:
        print(str(SkillsOfStudent[int(Num_of_Skills/2)]))
        print(str(SkillsOfStudent[int((Num_of_Skills/2)+1)]))

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.

if person.get('skills') is not None:
    if 'Python' in person.get('skills'):
        print('He is a developer')
    if {'JavaScript','React'} in person.get('skills'):
        print('He is a front end developer')
    elif {'Node', 'Python', 'MongoDB'} in person.get('skills'):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'} in person.get('skills'):
        print('He is a fullstack developer')
    else :
        print('unknown title')

if person.get('is_married') == True and person.get('country') == 'Finland':
    print(person.get('first_name') + ' ' + person.get('last_name') + ' lives in ' + person.get('country') + '. He is married')