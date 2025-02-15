universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students_list =[]
tuition_list=[]

print("****************************************")

def enrollment_stats(universities):
    total_students = 0
    total_tuition = 0
    for uni in universities:
        students_list.append(uni[1])
        tuition_list.append(uni[2])
        total_students+=uni[1]
        total_tuition+=uni[2]
    print(f"Total students: {total_students}")
    print(f"Total tuition: ${total_tuition}")
def mean(name,lists):
    total = 0
    for item in lists:
        total+=item
    print(f"{name}{round(total/len(lists),2)}")
def median(name,lists):
    if len(lists)%2==0:
        median = round(lists[len(lists)//2]+lists[len(lists)//2+1]/2,2)
        print(f"{name}{median}")
    else:
        print(f"{name}{lists[len(lists)//2+1]}")
enrollment_stats(universities)
print("")
print("")
mean("Student mean: ",students_list)
median("Student median: ",students_list)
print("")
print("")
mean("Tuition mean: $",tuition_list)
median("Tuition median: $",tuition_list)

print("****************************************")