import math

import matplotlib.pyplot as plt
import numpy as np

# Define constants
# numTimeSteps = int(input(""))  # Needed for Coursera automatic grading
numTimeSteps = 20
timeStep = 100
luminosity = 1350  # W/m2
albedo = 0.3
emissivity = 1
stefanBoltzmann = 5.67e-8  # W/m2 K4
initialTemperature = 0  # K
secondsInYear = 31536000  # s

waterDepth = 4000  # m
planetRadius = 6.37e6  # m
waterVolume = 4/3 * math.pi * (pow(waterDepth + planetRadius, 3) - pow(planetRadius, 3))  # m3
waterSurfaceArea = 4 * math.pi * pow(waterDepth + planetRadius, 2)  # m2
waterDensity = 997  # kg/m3
waterMass = waterVolume * waterDensity
waterSpecificHeatCapacity = 4200  # J/kg K
heatCapacity = waterSpecificHeatCapacity * waterMass / waterSurfaceArea  # J/m2 K

# Initialise simulation state
heatContents = []  # J/m2
temperatures = []  # K
outfluxes = []  # W/m2
heatFluxes = []  # W/m2
heatFluxesPerTimestep = []  # J/m2

influx = luminosity * (1 - albedo) / 4
temperatures.append(initialTemperature)
heatContents.append(initialTemperature * heatCapacity)
outfluxes.append(stefanBoltzmann * emissivity * pow(initialTemperature, 4))
heatFluxes.append(influx - outfluxes[0])
heatFluxesPerTimestep.append(heatFluxes[0] * secondsInYear)

# Iteratively apply state change equations
for _ in range(numTimeSteps):
    heatContents.append(heatContents[-1] + heatFluxesPerTimestep[-1] * timeStep)
    temperatures.append(heatContents[-1] / heatCapacity)
    outfluxes.append(stefanBoltzmann * emissivity * pow(temperatures[-1], 4))
    heatFluxes.append(influx - outfluxes[-1])
    heatFluxesPerTimestep.append(heatFluxes[-1] * secondsInYear)

# print(temperatures[-1], outfluxes[-1])  # Needed for Coursera automatic grading
plt.plot(np.arange(numTimeSteps + 1) * timeStep, temperatures)
plt.show()
