from datetime import date

def solution(a, b):
    answer = ''
    _list = ['MON','TUE','WED','THU','FRI','SAT','SUN']

    day = date(2016,a,b)
    answer = _list[day.weekday()]
    return answer