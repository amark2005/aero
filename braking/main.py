import numpy as np
init_u_kmh=150 #initial Speed of a car KM/H
u=np.round(init_u_kmh*(5/18),2)
fin_v_kmh=80 #target speed of a car KM/H
v=np.round(fin_v_kmh*(5/18))
a=-8 # Brake Decelartion of a car m/s^2 (should be negative)
m=825 # mass of a car KG
t=np.round((v-u)/a,2)
d=np.round((u*t)-0.5*(a*(t**2)),2)
F=m*a

print(f"u={u} | v={v} | a={a}")
print(f"Time to stop: {t} | Distance to stop: {d} | Force: {F*-1}")