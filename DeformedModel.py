import numpy as np
import math

''' Script that implements straightforward the simplified analytical model for the α
and Urel azimuthal variations under different yaw offsets given by the paper:
(Rick Damiani et. al, "Assessment of wind turbine component loads under
yaw-offset conditions" - 2018)
The script stands for evaluating the relevant system created in MATLAB/Simulink!
-- NOTES: 1) the parameters' values are selected randomly .. we MISS the equation
             for the U - (windSpeedElevation) and some units.
DEFORMED edition
'''

class AlternativeDeformedModel:
    def __init__(self, DENSITY, CL, GAMMA, DELTA, THETA, U_HUB, PSI, OMEGA, r, c):
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
        self.vt = 0
        self.U = 0
        self.PHI = 0
        self.ALPHA = 0
        self.U_REL = 0
        self.axial = 0

    def tangentialVelocity(self):
        self.vt = self.OMEGA * self.r * (2*np.pi/60)    # [m/sec]

    def windSpeedElevation(self):  # psi, U_hub, r should be included HERE .. we're waiting for the equation .. now we set it like that
        self.U = self.U_HUB          # [m/sec]

    def AngleOFAttack(self):
        self.PHI = math.atan((self.U * np.cos(self.GAMMA) * np.cos(self.DELTA)) / (
                    (self.vt - self.U) * (np.cos(self.GAMMA) * np.sin(self.DELTA) * np.sin(self.PSI) + np.sin(self.GAMMA) * np.cos(self.PSI))))    # [rad]
        print("PHI = ", self.PHI)
        self.ALPHA = self.PHI - self.THETA  # EQUATION 3   [rad]
        print("ALPHA = ", self.ALPHA)

    def airVelocityAirfoil(self):
        self.U_REL = np.sqrt((self.U * np.cos(self.GAMMA) * np.cos(self.DELTA)) ** 2 + (
                    (self.vt - self.U) * (np.cos(self.GAMMA) * np.sin(self.DELTA) * np.sin(self.PSI) + np.sin(self.GAMMA) * np.cos(self.PSI))) ** 2)  # EQUATION 4  [m/sec]
        print("U_REL = ", self.U_REL)

    def axialComponent(self):
        self.axial = 0.5 * self.DENSITY * (self.U_REL ** 2) * self.CL * self.ALPHA * self.c * np.cos(self.PHI)  # EQUATION 1
        print("FINAL RESULT is = ", self.axial)

    def runComputation(self):
        # run all methods sequentially
        self.tangentialVelocity()
        self.windSpeedElevation()
        self.AngleOFAttack()
        self.airVelocityAirfoil()
        self.axialComponent()

