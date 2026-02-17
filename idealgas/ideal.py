import numpy as np
import matplotlib.pyplot as plt

class ideal:
    R=8.314 #Joules/mol.K  Ideal Gas Constant

    def __init__(self):
        self.menu()

    def menu(self):
        while True:
            print("Ideal Gas")
            print("""
                1. Pressure(P)
                2. Volume(V)
                3. Moles(n)
                4. Temperature (T)
                5. Exit
                """)
            s=input("Enter your choice (1-5): ").strip()

            if s == "1":
                self.V=float(input("Volume(m3)?: "))
                self.n=float(input("Moles(mol)?: "))
                self.T=float(input("Temperature(Kelvin)?: "))
                ans=self.pressure()
                print(f"Pressure(Pa): {ans}")

            elif s == "2":
                self.P=float(input("Pressure(Pa)?: ")) 
                self.n=float(input("Moles(mol)?: "))
                self.T=float(input("Temperature(Kelvin)?: "))
                ans=self.volume()
                print(f"Volume(m3): {ans}")

            elif s == "3":
                self.P=float(input("Pressure(Pa)?: "))  
                self.V=float(input("Volume(m3)?: "))
                self.T=float(input("Temperature(Kelvin)?: "))
                ans=self.moles()
                print(f"Moles(mol): {ans}")

            elif s == "4":
                self.P=float(input("Pressure(Pa)?: "))
                self.V=float(input("Volume(m3)?: "))
                self.n=float(input("Moles(mol)?: "))
                ans=self.temp()
                print(f"Temperature(K): {ans}")

            elif s == "5":
                print("Bye")
                break

    def pressure(self):
        self.P=(self.n*self.R*self.T)/self.V
        return self.P

    def volume(self):
        self.V=(self.n*self.R*self.T)/self.P
        return self.V 

    def moles(self):
        self.n=(self.P*self.V)/(self.R*self.T)
        return self.n

    def temp(self):
        self.T=(self.P*self.V)/(self.n*self.R)
        return self.T

ideal()
