import numpy as np
from SimplifiedAnalyticalModel import SimplifiedAnalyticalModel

if __name__ == "__main__":
    # KNOWN VALUES HERE
    DENSITY = 1.225  # [kg/m^3]
    CL = 2 * np.pi  # [DON'T KNOW]
    GAMMA = 10  # [degrees]
    DELTA = 3  # [degrees]
    THETA = 5  # [degrees]
    U_HUB = 10  # [m/sec]
    PSI = 50  # [degrees]
    OMEGA = 8  # [RPM]
    r = 38.5  # [m]
    c = 1  # [DON'T KNOW]

    # CALL THE CLASS AND RUN TO SEE RESULTS
    model = SimplifiedAnalyticalModel(DENSITY, CL, GAMMA, DELTA, THETA, U_HUB, PSI, OMEGA, r, c)
    output = model.axialComponent()
    print("FINAL RESULT IS = ", output)