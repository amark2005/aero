import ctypes
import os
engine_path=os.path.join(os.getcwd(),"engine.so")
engine=ctypes.CDLL(engine_path)
engine.ctok.argtypes=[ctypes.c_double]
engine.ctok.restype=ctypes.c_double
engine.p2.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
engine.p2.restype = ctypes.c_double
def main():
    P1=int(input("Enter the Pressure 1: "))
    temp1=engine.ctok(float(input("Enter the Temperature in the pits: ")))
    temp2=engine.ctok(float(input("Enter the Temperature in the track: ")))   
    p2=engine.p2(P1,temp1,temp2)
    print(f"The Racing Pressure of the tire is: {round(p2,2)}")
    

main()

