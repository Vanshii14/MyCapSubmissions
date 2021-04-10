radius=input("Enter the radius of circle whose area is to be calculated : ")
radius=float(radius)
area=3.14*radius*radius
print("The area of circle with radius",radius," is ",area)


Fn=input("Enter the name of the file whose extension is to be printed : ")
File_Exten=Fn.split(".")
print("The Extension of the file name entered is : " + repr(File_Exten[-1])) 

