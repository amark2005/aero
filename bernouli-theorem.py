import numpy as np
import matplotlib.pyplot as plt
rho=1.225
def berno(v1,v2,rho):
    return 0.5*rho*(v2**2-v1**2)
def ms_to_kmh(ms):
    return ms*3.6
def kmh_to_ms(kmh):
    return kmh/3.6
ms=kmh_to_ms(90)
v_freestream=np.linspace(0,ms,100)
v_accelerated=v_freestream*1.5
delta_p=berno(v_freestream,v_accelerated,rho)
print(delta_p)
print(ms_to_kmh(v_freestream))
plt.figure(figsize=(8,4))
plt.plot(ms_to_kmh(v_freestream),delta_p)
plt.title("Bernouli's Theorem")
plt.xlabel("Freestream (km/h)")
plt.ylabel("Pressure Drop (pa)")
plt.grid(True)
plt.show()
