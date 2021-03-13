units = {"in": 0.0254,"ft":0.3048, "yd":0.9144, "mi":1609.34, "m": 1, "km": 1000}

user_distance = float(input("What is the distance? "))
starting_units = input("What are the starting units? ex: in, ft, yd, mi, m, km: ")
ending_units = input("What are the ending units? ex: in, ft, yd, mi, m, km: ")



print((units[starting_units]* user_distance)/units[ending_units])