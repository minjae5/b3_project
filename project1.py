import operator
import sys

def main():    
    f = open('students.txt','r') #students.txt 파일 읽기
    slist=[]
    while True:
        data = f.readline().split() #readline으로 data리스트에 넣음
        if not data:
            break

        avg = (int(data[3])+int(data[4]))/2
        
        if avg>90:
            grade='A'
        elif 80<=avg<90:
            grade='B'
        elif 70<=avg<80:
            grade='C'
        elif 60<=avg<70:
            grade='D'
        else:
            grade='F'

        avg = str(avg)

        stu = Student(data[0],data[1]+' '+data[2],data[3],data[4],avg,grade) #data를 Student클래스로 변환
        slist.append(stu) # slist에 stu클래스 객체 append
        if not data:
            break
        
        
    while True:
        choose=input('#select the function >> ') #function 선택
        if choose == 'show':
            show(slist)
        elif choose == 'search':
            search(slist)
        elif choose =='change_score':
            change_score(slist)
        elif choose =='search_grade':
            search_grade(slist)
        elif choose =='add':
            add(slist)
        elif choose =='remove':
            remove(slist)
        elif choose =='quit':
            quit(slist)

class Student:
    def __init__(self,snum,name,mid,fin,avg,grade):
        self.snum=snum
        self.name=name
        self.mid=mid
        self.fin=fin
        self.avg=avg
        self.grade=grade

def show(slist):
    slist.sort(key=operator.attrgetter('avg'),reverse=True) #operator모듈로 내림차순 sort
    print('Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade')
    print('-----------------------------------------------------------')
    for i in range(len(slist)):
        print(slist[i].snum+'\t'+slist[i].name+'\t'+slist[i].mid+'\t'+slist[i].fin+'\t'+slist[i].avg+'\t'+slist[i].grade) #slist객체 속성 출력
    print('-----------------------------------------------------------')   

def search(slist):
    input_snum = input('Student ID: ')
    check=0
    print('Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade')
    print('-----------------------------------------------------------')
    for i in range(len(slist)): #입력받은 Student ID 객체 탐색
        if slist[i].snum == input_snum:
            check=1
            
            print(slist[i].snum+'\t'+slist[i].name+'\t'+slist[i].mid+'\t'+slist[i].fin+'\t'+slist[i].avg+'\t'+slist[i].grade)
    print('-----------------------------------------------------------')
    if check==0:
        print('NO SUCH PERSON')

def change_score(slist):
    input_snum = input('Student ID: ')
    check=1
    for i in range(len(slist)):
        if slist[i].snum == input_snum:
            check=1
            mid_fin=input('mid/fin?: ')
            if mid_fin == 'mid':
                new_score=input('Input new score: ')
                print('Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade')
                print('-----------------------------------------------------------')
                print(slist[i].snum+'\t'+slist[i].name+'\t'+slist[i].mid+'\t'+slist[i].fin+'\t'+slist[i].avg+'\t'+slist[i].grade)
                slist[i].mid = new_score #입력받은 score로 객체의 mid속성 변경
                print('Score changed')    
                
                
            elif mid_fin == 'fin':
                new_score=input('Input new score: ')
                print('Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade')
                print('-----------------------------------------------------------')
                print(slist[i].snum+'\t'+slist[i].name+'\t'+slist[i].mid+'\t'+slist[i].fin+'\t'+slist[i].avg+'\t'+slist[i].grade)
                slist[i].fin = new_score #입력받은 score로 객체의 mid속성 변경
                print('-Score changed-')    
                
            
            avg = (int(slist[i].mid)+int(slist[i].fin))/2
            
            slist[i].avg = str(avg)
            slist[i].grade = my_grade(avg)
            
            print(slist[i].snum+'\t'+slist[i].name+'\t'+slist[i].mid+'\t'+slist[i].fin+'\t'+slist[i].avg+'\t'+slist[i].grade)
            print('-----------------------------------------------------------')
    
    if check==0:
        print('NO SUCH PERSON')

def add(slist):
    input_snum = input('Student ID: ')
    for i in range(len(slist)):
        if slist[i].snum == input_snum:
            print('ALREADY EXISTS.')
            return
            
            
    new_name = input('Name: ')
    new_mid = input('Midterm Score: ')
    new_fin = input('Final Score: ')
    
    avg = (int(new_mid)+int(new_fin))/2
    grade=my_grade(avg)
    avg=str(avg)
    stu = Student(input_snum,new_name,new_mid,new_fin,avg,grade) #입력받은 값들로 새로운 Student객체 생성
    slist.append(stu) #stu객체 slist에 append
    
    print('Student added')

def my_grade(avg): #avg 매개변수로 받으면 grade 리턴
    if avg>90:
        grade='A'
    elif 80<=avg<90:
        grade='B'
    elif 70<=avg<80:
        grade='C'
    elif 60<=avg<70:
        grade='D'
    else:
        grade='F'
    return grade

def search_grade(slist):
    input_grade = input('Grade to search: ')
    count=0
    print('Student\t\tName\t\tMidterm\tFinal\tAverage\tGrade')
    print('-----------------------------------------------------------')
    for i in range(len(slist)):
        if slist[i].grade == input_grade: #입력받은 grade에 해당되는 객체 탐색
            count=1
            print(slist[i].snum+'\t'+slist[i].name+'\t'+slist[i].mid+'\t'+slist[i].fin+'\t'+slist[i].avg+'\t'+slist[i].grade)
    print('-----------------------------------------------------------')
    if count==0:
        print('NO RESULTS')
        return

def remove(slist):
    input_snum = input('Student ID: ')
    check=False
    for i in range(len(slist)):
        if slist[i].snum == input_snum: #입력받은 snum에 해당되는 객체 탐색
            check=True
            del slist[i] #해당 객체 삭제
            print('Student removed')
            return
    if check ==False:
        print('NO SUCH PERSON')

def quit(slist):
    quit_=input('Save data?[yes/no]: ')
    
    if quit_ == 'yes':
        file_name=input('File name?: ')
        fn = open(file_name,'w') #입력받은 file_name으로 파일 생성 및 열기
        for i in range(len(slist)): #slist객체속성들을 파일에 쓰기
            fn.write(slist[i].snum)
            fn.write(' ')
            fn.write(slist[i].name)
            fn.write(' ')
            fn.write(slist[i].mid)
            fn.write(' ')
            fn.write(slist[i].fin)
            fn.write(' ')
            fn.write(slist[i].avg)
            fn.write(' ')
            fn.write(slist[i].grade)
            fn.write('\n')
        fn.close()
    elif quit_ == 'no': #no입력받을시 함수 종료
        
        exit()

if __name__ == "__main__": #main()함수 호출
    main()

