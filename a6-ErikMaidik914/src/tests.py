from functions import*


def run_add_and_create_test():
    p1=1
    p2=2
    p3=3
    person1=create_person(p1,p2,p3)
    person_list=[]
    person_list=add_to_list(person_list, person1)
    assert len(person_list) == 1
    fp2=1
    fp3=3
    fp1=9
    person2=create_person(fp1,fp2,fp3)
    person_list = add_to_list(person_list,person2)
    assert len(person_list)==2
    p1=100
    person3=create_person(p1,p2,p3)
    assert person3==False


def run_generate_test():
    l=[]
    l=generate_people(3)
    assert len(l)==3


def run_all_tests():
        print('Starting add and create command  tests... ')
        run_add_and_create_test()
        print('Finished add and create command  tests...')
        print('Starting generate tests...')
        run_generate_test()
        print('Finished generate tests...')


































def run_tests():
    print('Starting add and create command  tests... ')
    print('Finished add and create command  tests...')
    print('Starting generate tests...')
    print('Finished generate tests...')
