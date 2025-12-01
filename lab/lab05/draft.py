def safe_div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
def to_int(x):
    try:
        return int(x)
    except ValueError:
        return "valueError"
    except TypeError:
        return 'TypeError'
    
def read_number(path:str):
    try:
        f = open(path)           # 可能 FileNotFoundError
        data = f.read()        
        num = int(data)          # 可能 ValueError
    except FileNotFoundError:
        return "FileNotFoundError"
    except TypeError:
        return "Not a number"
    else:
        return num
    finally:
        print("Done")
