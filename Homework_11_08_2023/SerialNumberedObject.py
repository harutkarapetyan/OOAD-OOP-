class SerialNumberedObject:
    count = 0
    
    def __init__(self):
        SerialNumberedObject.count += 1
        
        
    def get_serial_number(self):
        return   self.count
    
ob1 = SerialNumberedObject()

print(f"I am object number {ob1.get_serial_number()}")      

ob2 = SerialNumberedObject()
print(f"I am object number {ob2.get_serial_number()}")        