from logging import *
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
    print('branch and group added')    



    for i in range(20):
        inst_name = 'dr '+r_name(3)
        I = Instractor(name=inst_name, e_mail=inst_name[3]+str(randint(10, 99)))
        I.save()
    print('instractor added')    

    groups = Group.objects.all()
    for g in groups:
        for i in range(20):
            s_name = r_name(4)
            s = Student(name=s_name, e_mail='stu'+s_name[0]+str(randint(1000, 9999)), group=g)
            s.save()
    print('students added')    

    tags = ['embedded', 'python', 'machine learning', 'computer vision', 'space',
            'scince', 'web', 'iot']

    for tag in tags:
        t = Tag(name = tag)
        t.save()
    print('tags added')    

    
    groups = Group.objects.all()
    tags = Tag.objects.all()
    instractors = Instractor.objects.all()
    for group in groups:
        for i in range(5):
            students = Student.objects.filter(group=group)
            project = Project(title='project #'+str(i),
                              description='prject #'+str(i)+' decription')
            project.save()            
            project.tags.set(tags[randint(0, int((len(tags)-1)/2)):
                                  randint(int(len(tags)/2), len(tags))])
            project.students.set(students)
            r_inst = randint(0, len(instractors)-3)
            project.instractors.set(instractors[r_inst: r_inst+2])
            project.group.add(group)
            project.save()
            print('a project added')
            child_n = randint(1, 5)
            for j in range(child_n):
                stus = Student.objects.filter(project=project)
                stus_l = len(stus)
                insts = Instractor.objects.filter(project=project)

                #TODO fix students devide to parts for projects 
                childproject = Project(title='child project #'+str(j),
                                       description = 'child prject #'+str(j)+' decription',
                                       parent=project)
                childproject.save()
                childproject.group.add(group)
                childproject.students.set(stus[int((j/child_n)*stus_l):
                                               int(((j+1)/child_n)*stus_l)] )
                childproject.instractors.set(insts)
                childproject.save()

main()
