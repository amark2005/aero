import numpy as np
delta_v=9300
Isp=200
g0=9.81
m0=10
m_f=4
print(f"The delta V : {delta_v}m/s")
m0_m_f=np.round(np.exp(delta_v/(Isp*g0)),2)
delta_v=np.round(Isp*g0*(np.log(m0_m_f)),2)
#print("delta_v/Isp*g0:",delta_v/(Isp*g0))
print(delta_v)
print(m0_m_f)