def _avg(scores):
    return sum(scores) / len(scores)

def class_avg(students):
    for scores in students.values():
        print(_avg(scores))
