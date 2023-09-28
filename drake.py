def hamster(animal_type,breed,age,sex='male'):
    print('this is a ',animal_type,' of breed ',breed,'. it is ',sex,' whose age is ',age)

drake = hamster('rat','caucassian','1.2 years','female')
print(drake)

def make_pizza(*toppings):
    print(toppings)

make_pizza('1','2','3','4')

def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('a','b',location = 'prind', field = '[ddd')
print(user_profile)
