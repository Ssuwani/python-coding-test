from datetime import datetime
x, y = map(int, input().split())
day_name = {
    1: "TUE",
    2: "WED",
    3: "THU",
    4: "FRI",
    5: "SAT",
    6: "SUN",
    7: "MON",

}
print(day_name[datetime(2017, x, y).isoweekday()])
