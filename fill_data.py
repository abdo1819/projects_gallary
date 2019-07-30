from viewer_core.models import Group,Branch,Instractor,Student
from viewer_core.models import Project,Tag

from random import randint

def r_name(n):
    ''' generate random name with n words '''
    names = ['mohamed', 'ahmed', 'ali', 'abdo', 'bassem', 'gamal', 'mostafa']
    random_name=names[randint(0,len(names)-1)]
    for i in range(n-1):
        random_name = random_name +' '+ names[randint(0,len(names)-1)]
    return random_name

def main():
    branch_names = ["power", "communication", "computer"]
    group_names = ['first', 'second', 'therd', 'forth']

    for branch_name in branch_names:
        b = Branch(name=branch_name)
        b.save()
        for group_name in group_names:
            g = Group(name=group_name, branch=b)
            g.save()




    for i in range(20):
        inst_name = 'dr '+r_name(3)
        I = Instractor(name=inst_name, e_mail=inst_name[3]+str(randint(10, 99)))
        I.save()

    groups = Group.objects.all()
    for g in groups:
        for i in range(20):
            s_name = r_name(4)
            s = Student(name=s_name, e_mail='stu'+s_name[0]+str(randint(1000, 9999)), group=g)
            s.save()
