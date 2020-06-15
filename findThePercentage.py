if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        #Multiple inputs will go in line as * is applied.
        name, *line = input().split()
        #change it to a list of floats.
        #inputs are iterable hence map can be used to change every element of lune to float
        #converting to list is important since map object cannot be used for iteration.
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ss = []
    if query_name in student_marks:
        ss = student_marks[query_name]
    
    avg = sum(ss)/len(ss)
    print("{:.2f}".format(avg))