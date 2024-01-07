def same_by(characteristic, objects):
    if len(objects)==0:
        return True
    obj=characteristic(objects[0])
    for i in range(len(objects)):
        if obj!=characteristic(objects[i]):
            return False
    return True


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print("same")
else:
    print("different")