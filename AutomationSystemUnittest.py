import unittest
from SmartHome import SmartLight, Thermostat, SecurityCamera, AutomationSystem

class TestAutomationSystem(unittest.TestCase):
    def setUp(self):
        light = SmartLight(1, "off", 20)
        thermostat = Thermostat(1, "off", 20)
        camera = SecurityCamera(1, "on", "ON")

        self.automationSystem = AutomationSystem([light], [thermostat], [camera])

    def testAddDevicesToDataset(self):
        light2 = SmartLight(2, "off", 50)
        self.automationSystem.addDevicesToTheDataset(light2)

        self.assertIn(light2, self.automationSystem.lights)

    def testSetupRoom(self):
        room = self.automationSystem.setupRoom(1)

        self.assertEqual(room[0], self.automationSystem.lights[0])
        self.assertEqual(room[1], self.automationSystem.thermostats[0])
        self.assertEqual(room[2], self.automationSystem.cameras[0])

    def testCheckDevicesStatus(self):
        roomLight = self.automationSystem.lights[0]
        roomThermostat = self.automationSystem.thermostats[0]
        roomCamera = self.automationSystem.cameras[0]

        status = self.automationSystem.checkDevicesStatus(roomLight, roomThermostat, roomCamera)

        self.assertTrue(status)

    def testRandomMotionDetection(self):
        roomCamera = self.automationSystem.cameras[0]
        original_status = roomCamera.getSecurityStatus()
        self.automationSystem.randomMotionDetection(roomCamera)

        self.assertNotEqual(original_status, roomCamera.getSecurityStatus())

    def testDeviceActions(self):
        roomLight = self.automationSystem.lights[0]
        roomThermostat = self.automationSystem.thermostats[0]
        roomCamera = self.automationSystem.cameras[0]

        originalBrightness = roomLight.getBrightness()
        originalTemperature = roomThermostat.getTemperature()
        
        roomCamera.setSecurityStatus("OFF")

        self.automationSystem.deviceActions(roomLight, roomThermostat, roomCamera)

        self.assertEqual(originalBrightness, roomLight.getBrightness())
        self.assertEqual(originalTemperature, roomThermostat.getTemperature())

if __name__ == '__main__':
    unittest.main()
