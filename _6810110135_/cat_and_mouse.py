def cat_and_mouse(x:int, y:int, z:int ) -> str:
    if abs(x-z) == abs(y-z):
        return "Mouse C" 
    elif abs(x-z) < abs(y-z):
        return "Cat A"
    elif abs(x-z) > abs(y-z):
        return "Cat B"

if __name__ == "__main__":
    line_str = input("Enter A B C: ")
    line = map(int, line_str.split())
    result = cat_and_mouse(*line)
    print(result)