import unittest
from SmartHome import SmartLight, Thermostat, SecurityCamera, RandomSimulation

class TestAutomation(unittest.TestCase):
    def testSmartLightBrightness(self):
        light = SmartLight(1, "off", 100)

        simulation = RandomSimulation(light, None, None)
        simulation.startLightSimulation()
        
        self.assertTrue(0 <= light.getBrightness() <= 100)

    def testThermostatTemperature(self):
        thermostat = Thermostat(1, "off", 20)
    
        simulation = RandomSimulation(None, thermostat, None)
        simulation.startThermostatSimulation()
        
        self.assertTrue(-10 <= thermostat.getTemperature() <= 40)

    def testSecurityCameraStatus(self):
        camera = SecurityCamera(1, "off", "ON")

        simulation = RandomSimulation(None, None, camera)
        simulation.startCameraSimulation()
        
        self.assertIn(camera.getSecurityStatus(), ["ON", "OFF"])

if __name__ == '__main__':
    unittest.main()