import process
try:
    total = str(process.total)
    print("You got ",total, "fruits!")
except Exception as e:
    print("\33[41m[error]\33[0m Failed in getting total")
