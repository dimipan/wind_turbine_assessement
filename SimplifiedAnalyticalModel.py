import numpy as np
import math

''' Script that implements straightforward the simplified analytical model for the α
and Urel azimuthal variations under different yaw offsets given by the paper:
(Rick Damiani et. al, "Assessment of wind turbine component loads under
yaw-offset conditions" - 2018)
The script stands for evaluating the relevant system created in MATLAB/Simulink!
-- NOTES: 1) the parameters' values are selected randomly .. we MISS the equation
             for the U - (windSpeedElevation) and some units.
'''

class SimplifiedAnalyticalModel:
    def __init__(self):
        radians = np.pi / 180
        self.DENSITY = DENSITY          # [kg/m^3]
        self.CL = CL                    # DON'T KNOW
        self.GAMMA = GAMMA * radians    # [rad]
        self.DELTA = DELTA * radians    # [rad]
        self.THETA = THETA * radians    # [rad]
        self.U_HUB = U_HUB              # [m/sec]
        self.PSI = PSI * radians        # [rad]
        self.OMEGA = OMEGA              # [RPM]
        self.r = r                      # [m]
        self.c = c                      # DON'T KNOW

    def tangentialVelocity(self):
        vt = self.OMEGA * self.r * (2*np.pi/60)    # [m/sec]
        return vt

    def windSpeedElevation(self):  # psi, U_hub, r should be included HERE .. we're waiting for the equation .. now we set it like that
        U = self.U_HUB          # [m/sec]
        return U

    def AngleOFAttack(self):
        vt = self.tangentialVelocity()
        U = self.windSpeedElevation()
        PHI = math.atan((U * np.cos(self.GAMMA) * np.cos(self.DELTA)) / (
                    (vt - U) * (np.cos(self.GAMMA) * np.sin(self.DELTA) * np.sin(self.PSI) + np.sin(self.GAMMA) * np.cos(self.PSI))))    # [rad]
        print("PHI = ", PHI)
        ALPHA = PHI - self.THETA  # EQUATION 3   [rad]
        print("ALPHA = ", ALPHA)
        return PHI, ALPHA

    def airVelocityAirfoil(self):
        vt = self.tangentialVelocity()
        U = self.windSpeedElevation()
        U_REL = np.sqrt((U * np.cos(self.GAMMA) * np.cos(self.DELTA)) ** 2 + (
                    (vt - U) * (np.cos(self.GAMMA) * np.sin(self.DELTA) * np.sin(self.PSI) + np.sin(self.GAMMA) * np.cos(self.PSI))) ** 2)  # EQUATION 4  [m/sec]
        print("U_REL = ", U_REL)
        return U_REL

    def axialComponent(self):
        PHI, ALPHA = self.AngleOFAttack()
        U_REL = self.airVelocityAirfoil()
        axial = 0.5 * self.DENSITY * (U_REL ** 2) * self.CL * ALPHA * self.c * np.cos(PHI)  # EQUATION 1
        return axial

# KNOWN VALUES HERE
DENSITY = 1.225     # [kg/m^3]
CL = 2 * np.pi      # [DON'T KNOW]
GAMMA = 10          # [degrees]
DELTA = 3           # [degrees]
THETA = 5           # [degrees]
U_HUB = 10          # [m/sec]
PSI = 50            # [degrees]
OMEGA = 8           # [RPM]
r = 38.5            # [m]
c = 1               # [DON'T KNOW]

# CALL THE CLASS AND RUN TO SEE RESULTS
model = SimplifiedAnalyticalModel()
output = model.axialComponent()
print("FINAL RESULT IS = ", output)
