students =[
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def student_names(slists):
    for student in slists:
        print (student['first_name'] + ' '+ student['last_name'])


student_names(students)



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def studentANDinstruct (sandi):
    for group in sandi:
        counter = 0
        print (group)
        for person in sandi[group]:
            length = len(person['first_name']) + len(person['last_name'])
            counter += 1
            print str(counter) + ' - ' + person['first_name'] + ' '+ person['last_name'] + ' -', length


studentANDinstruct(users)