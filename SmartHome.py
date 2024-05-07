import random
import time
import tkinter as tk

class SmartLight:
    def __init__(self, id, status, brightness):
        self.id = id
        self.status = status
        self.brightness = int(brightness)

    def getDeviceType(self):
        return "Smart Light"
    
    def getID(self):
        return self.id

    def getStatus(self):
        return self.status
    
    def getBrightness(self):
        return self.brightness

    def turnOn(self):
        if self.status == "on":
            print("Light is already", self.status,"!")
            return
        
        currentBrightness = 0
        maxBrightness = self.brightness

        for _ in range(0, maxBrightness):
            currentBrightness += 1
        
        self.status = "on"
        print("Light is", self.status,"!")

    def turnOff(self):
        if self.status == "off":
            print("Light is already", self.status,"!")
            return
        
        currentBrightness = self.brightness
        
        maxBrightness = currentBrightness
        
        for _ in range(0, maxBrightness):
            currentBrightness -= 1
        
        self.status = "off"
        print("Light is", self.status,"!")

    def setBrightness(self, brightness):
        if self.status == "off":
            print("Error! Light is", self.status, "!")
            return
        
        if brightness <= 0:
            print("ERROR! Brightness can not be less than 0!")
            return
        
        self.brightness = int(brightness)
        print("Light's brightness has been set to", self.brightness)

class Thermostat:
    def __init__(self, id, status, temperature):
        self.id = id
        self.status = status
        self.temperature = int(temperature)

    def getDeviceType(self):
        return "Thermostat"
    
    def getID(self):
        return self.id

    def getStatus(self):
        return self.status
    
    def getTemperature(self):
        return self.temperature

    def turnOn(self):
        if self.status == "on":
            print("Thermostat is already", self.status,"!")
            return
        
        self.status = "on"

    def turnOff(self):
        if self.status == "off":
            print("Thermostat is already", self.status,"!")
            return
        
        self.status = "off"

    def setTemperature(self, temperature):
        if self.status == "off":
            print("ERROR! Thermostat is off!")
            return
        
        minTemp = -10
        maxTemp = 40

        if temperature < minTemp or temperature > maxTemp:
            print("ERROR! The given number is out of thermostat's range!")
            return
        
        if self.temperature == int(temperature):
            print("Temperature is already set to", int(self.temperature),"!")
            return

        self.temperature = int(temperature)
        print("New temperature is", self.temperature)
                
class SecurityCamera:
    def __init__(self, id, status, securityStatus):
        self.id = id
        self.status = status
        self.securityStatus = securityStatus

    def getDeviceType(self):
        return "Security Camera"
    
    def getID(self):
        return self.id

    def getStatus(self):
        return self.status

    def getSecurityStatus(self):
        return self.securityStatus

    def turnOn(self):
        if self.status == "on":
            print("Camera is already", self.status, "!")
            return
        
        self.status = "on"
        print("Camera is", self.status,"!")

    def turnOff(self):
        if self.status == "off":
            print("Camera is already", self.status, "!")
            return

        self.status = "off"
        print("Camera is", self.status,"!")

    def setSecurityStatus(self, securityStatus):
        if self.status == "off":
            print("ERROR! Camera is off!")
            return
        
        if securityStatus not in ("ON", "OFF"):
            print("ERROR! Invalid security status. Valid values are 'ON' and 'OFF'.")
            return
        
        if self.securityStatus == securityStatus:
            print("Security status is already", self.securityStatus,"!")
            return
        
        self.securityStatus = securityStatus
        print("Secturity status is", securityStatus,"!")

class RandomSimulation:
    def __init__ (self, light, thermostat, camera):
        self.light = light
        self.thermostat = thermostat
        self.camera = camera

    def startLightSimulation(self):
        for _ in range (0, 10):
            randomStatus = random.choice(["on", "off"])
            
            if randomStatus == "on":
                self.light.turnOn()
            else:
                self.light.turnOff()

            newBrightness = random.uniform(0, 100)
            self.light.setBrightness(newBrightness)

            time.sleep(1)

        print("Light simulation has ended!")

    def startThermostatSimulation(self):
        for _ in range (0, 10):
            randomStatus = random.choice(["on", "off"])
            
            if randomStatus == "on":
                self.thermostat.turnOn()
            else: self.thermostat.turnOff()

            newTemperature = random.uniform(-10, 40)
            self.thermostat.setTemperature(newTemperature)

            time.sleep(1)

        print("Thermostat simulation has ended!")

    def startCameraSimulation(self):
        for _ in range (0, 10):
            randomStatus = random.choice(["on", "off"])
            
            if randomStatus == "on":
                self.camera.turnOn()
            else: self.camera.turnOff()

            securityStatus = random.choice(["ON", "OFF"])
            
            self.camera.setSecurityStatus(securityStatus)

            time.sleep(1)

        print("Camera simulation has ended!")
        
'''Part 1
light = SmartLight(1, "off", 100)
thermostat = Thermostat(1, "off", 20)
camera = SecurityCamera(1, "off", "ON")

simulation = RandomSimulation(light, thermostat, camera)

simulation.startLightSimulation()
simulation.startThermostatSimulation()
simulation.startCameraSimulation()
'''

class AutomationSystem:
    def __init__ (self, lights, thermostats, cameras):
        self.lights = lights
        self.thermostats = thermostats
        self.cameras = cameras

    def getLights(self):
        return self.lights
    
    def getLights(self):
        return self.thermostats
    
    def getLights(self):
        return self.cameras
    
    # Adds more devices to the dataset
    def addDevicesToTheDataset(self, newDevice):
        if newDevice.getDeviceType() == "Smart Light" and newDevice not in self.lights:
            self.lights.append(newDevice)
            print("Device", newDevice.getDeviceType(), "With id:", newDevice.getID(),"has been added to the dataset!")
            return
        
        elif newDevice.getDeviceType() == "Thermostat" and newDevice not in self.thermostats:
            self.thermostats.append(newDevice)
            print("Device", newDevice.getDeviceType(), "With id:", newDevice.getID(),"has been added to the dataset!")
            return
        
        elif newDevice.getDeviceType() == "Security Camera" and newDevice not in self.cameras:
            self.cameras.append(newDevice)
            print("Device", newDevice.getDeviceType(), "With id:", newDevice.getID(),"has been added to the dataset!")
            return

        print("WARNING! Device", newDevice.getDeviceType(), "With id:", newDevice.getID(),"Already exists in the dataset!")

    # Groups the devices for each room based on their ID. Each ID is one room.
    def setupRoom(self, id):
        room = [None, None, None]

        for device in self.lights:
            if device.getDeviceType() == "Smart Light" and device.getID() == id:
                room[0] = device
                break

        for device in self.thermostats:
            if device.getDeviceType() == "Thermostat" and device.getID() == id:
                room[1] = device
                break

        for device in self.cameras:
            if device.getDeviceType() == "Security Camera" and device.getID() == id:
                room[2] = device
                break

        return room

    # Checks the initial device status. If the camera is off then the automation task won't start.
    def checkDevicesStatus(self, roomLight, roomThermostat, roomCamera):
        if roomCamera.getStatus() == "off":
            print("ERROR! Can not continue task if camera is off!")
            return False
        
        if roomLight.getStatus() == "off":
            roomLight.turnOn()

        if roomThermostat.getStatus() == "off":
            roomThermostat.turnOn()

        return True
    
    # Simulates motion detection based on a random number.
    def randomMotionDetection(self, roomCamera):
        randomMotionLevel = int(random.uniform(0, 10))
        
        if randomMotionLevel < 5 and randomMotionLevel >= 0:
            roomCamera.setSecurityStatus("OFF")
        
        if randomMotionLevel >= 5 and randomMotionLevel <= 10:
            roomCamera.setSecurityStatus("ON")
    
    # Depending on the motion level, the light's brightness and temperature changes
    def deviceActions(self, roomLight, roomThermostat, roomCamera):
        if roomCamera.getSecurityStatus() == "OFF":
            roomLight.setBrightness(20)
            roomThermostat.setTemperature(20)
        
        if roomCamera.getSecurityStatus() == "ON":
            roomLight.setBrightness(100)
            roomThermostat.setTemperature(-10)
    
    # Executes the automation task with the help of the functions above. 'id' parameter is the id of the devices which represents a room.
    def automationTask(self, id):
        room = self.setupRoom(id)
        roomLight = room[0]
        roomThermostat = room[1]
        roomCamera = room[2]

        status = self.checkDevicesStatus(roomLight, roomThermostat, roomCamera)
        
        if status == False:
            return

        for i in range(0, 10):
            self.randomMotionDetection(roomCamera)

            self.deviceActions(roomLight, roomThermostat, roomCamera)
            
            print("Room ID:",id,"\n",
            "Security Status:", roomCamera.getSecurityStatus(), "\n",
            "Smart Light:", roomLight.getBrightness(), "\n",
            "Temperature:", roomThermostat.getTemperature())

            print("Round", i+1, "Completed!","\n")
            time.sleep(3)

'''Part 2
light1 = SmartLight(1, "on", 10)
light2 = SmartLight(2, "on", 10)
light3 = SmartLight(3, "off", 10)

lights = [
    light1,
    light2,
    light3
]

thermostat1 = Thermostat(1, "off", 20)
thermostat2 = Thermostat(2, "on", 20)
thermostat3 = Thermostat(3, "on", 20)

thermostats = [
    thermostat1,
    thermostat2,
    thermostat3
]

camera1 = SecurityCamera(1, "on", "OFF")
camera2 = SecurityCamera(2, "on", "OFF")
camera3 = SecurityCamera(3, "on", "ON")

cameras = [
    camera1,
    camera2,
    camera3
]

automationSystem = AutomationSystem(lights, thermostats, cameras)

light4 = SmartLight(4, "off", 50)
automationSystem.addDevicesToTheDataset(light4)

thermostat4 = Thermostat(4, "off", -9)
automationSystem.addDevicesToTheDataset(thermostat4)

camera4 = SecurityCamera(4, "off", "ON")
automationSystem.addDevicesToTheDataset(camera4)

automationSystem.addDevicesToTheDataset(light1)
automationSystem.addDevicesToTheDataset(thermostat2)
automationSystem.addDevicesToTheDataset(camera3)
print("Adding new devices process has been completed!\n")

# Automation System starts tasks for 4 different rooms.
#automationSystem.automationTask(1)
#print("Room 1 automation task has been completed!\n")
#time.sleep(1)

#automationSystem.automationTask(2)
#print("Room 2 automation task has been completed!\n")
#time.sleep(1)

#automationSystem.automationTask(3)
#print("Room 3 automation task has been completed!\n")
#time.sleep(1)

#automationSystem.automationTask(4)
#print("Room 4 automation task has been completed!\n")
#time.sleep(1)
'''

'''Part 4
'''
class SmartHomeGUI:
    def __init__(self, root, light, thermostat, camera):
        self.root = root
        self.light = light
        self.thermostat = thermostat
        self.camera = camera

        self.textPanel = tk.Text(root, height=22, width=100)
        self.textPanel.pack()

        self.creatingUI()

    def creatingUI(self):
        clearFrame = tk.Frame(self.root)
        clearFrame.pack()

        clearButton = tk.Button(self.root, text="Clear Log", command=self.clearLog)
        clearButton.pack()

        lightFrame = tk.Frame(self.root)
        lightFrame.pack()

        lightLabel = tk.Label(lightFrame, text="Light Settings")
        lightLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        lightOnButton = tk.Button(self.root, text="Turn Light On/Off", command=self.lightSwitch)
        lightOnButton.pack()

        self.brightnessScale = tk.Scale(self.root, from_=0, to=100, orient="horizontal", length=200, label="Set Brightness", command=self.updateBrightness)
        self.brightnessScale.pack()
        self.brightnessScale.set(0)

        thermostatFrame = tk.Frame(self.root)
        thermostatFrame.pack()

        thermostatLabel = tk.Label(thermostatFrame, text="Thermostat Settings")
        thermostatLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        thermostatOnButton = tk.Button(self.root, text="Turn Thermostat On/Off", command=self.thermostatSwitch)
        thermostatOnButton.pack()

        self.temperatureScale = tk.Scale(self.root, from_=-10, to=40, orient="horizontal", length=200, label="Set Temperature", command=self.updateTemperature)
        self.temperatureScale.pack()
        self.temperatureScale.set(0)

        cameraFrame = tk.Frame(self.root)
        cameraFrame.pack()

        cameraLabel = tk.Label(cameraFrame, text="Camera Settings")
        cameraLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        cameraOnButton = tk.Button(self.root, text="Turn Camera On/Off", command=self.cameraSwitch)
        cameraOnButton.pack()

        securityStatusScale = tk.Button(self.root, text="Toggle Security Status", command=self.securityStatusSwitch)
        securityStatusScale.pack()

        automationFrame = tk.Frame(self.root)
        automationFrame.pack()

        automationLabel = tk.Label(automationFrame, text="Automation Task")
        automationLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        automationRuleFrame = tk.Frame(self.root)
        automationRuleFrame.pack()

        automationTaskButton = tk.Button(self.root, text="Start An Automation Task", command=self.automationTask)
        automationTaskButton.pack()

        automationRuleLabel = tk.Label(automationRuleFrame, text="Automation Rule: The process starts if and only if the camera is on based on a radndom motion detection level!")
        automationRuleLabel.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    def clearLog(self):
        self.textPanel.delete(1.0, tk.END)

    def lightSwitch(self):
        if self.light.status == "on":
            self.light.turnOff()
            self.appendMessage("Light is off!")
        else:
            self.light.turnOn()
            self.appendMessage("Light is on!")
    
    def updateBrightness(self, event=None):
        if self.camera.status == "on":
            if self.light.getStatus() == "on":
                brightness = self.brightnessScale.get()
                self.light.setBrightness(brightness)
                
                message = "Brightness is: " + str(self.light.getBrightness())

            else: message = "ERROR: Can not change brightness while the light is off!"

        else: message = "ERROR: Can not change brightness while camera is off!"

        self.appendMessage(message)

    def thermostatSwitch(self):
        if self.thermostat.status == "on":
            self.thermostat.turnOff()
            self.appendMessage("Thermostat is off!")
        else:
            self.thermostat.turnOn()
            self.appendMessage("Thermostat is on!")

    def updateTemperature(self,event=None):
        if self.camera.status == "on":
            if self.thermostat.getStatus() == "on":
                temperature = self.temperatureScale.get()
                self.thermostat.setTemperature(temperature)
                
                message = "Temperature is: " + str(temperature)

            else: message = "ERROR: Can not change temperature while the thermostat is off!"

        else: message = "ERROR: Can not change temperature while camera is off!"

        self.appendMessage(message)

    def cameraSwitch(self):
        if self.camera.status == "on":
            self.camera.turnOff()
            self.appendMessage("Camera is off!")
        else:
            self.camera.turnOn()
            self.appendMessage("Camera is on!")

    def securityStatusSwitch(self, event=None):
        if self.camera.status == "on":
            if self.camera.getSecurityStatus() == "OFF":
                self.camera.setSecurityStatus("ON")

            else: self.camera.setSecurityStatus("OFF")
            
            message = "Security status is: " + self.camera.securityStatus

        else: message = "ERROR: Can not change security status while the camera is off!"

        self.appendMessage(message)

    def appendMessage(self, message):
        self.textPanel.insert(tk.END, message + "\n")

    def automationTask(self):
        if self.camera.status == "on":
            if self.light.getStatus() == "on" and self.thermostat.getStatus() == "on":
                randomMotionLevel = int(random.uniform(0, 10))
        
                if randomMotionLevel < 5 and randomMotionLevel >= 0:
                    self.camera.setSecurityStatus("OFF")
                    self.light.setBrightness(20)
                    self.thermostat.setTemperature(20)

                if randomMotionLevel >= 5 and randomMotionLevel <= 10:
                    self.camera.setSecurityStatus("ON")
                    self.light.setBrightness(100)
                    self.thermostat.setTemperature(-10)

                message = "Security status is: " + str(self.camera.getSecurityStatus())
                self.appendMessage(message)

                message = "Brightness is: " + str(self.light.getBrightness())
                self.appendMessage(message)

                message = "Temperature is: " + str(self.thermostat.getTemperature())
                self.appendMessage(message)
            else:
                message = "ERROR: Can not change brightness/temperature while the light/thermostat is off!"
                self.appendMessage(message)

        else: 
            message = "ERROR: Can not start an automation task while camera is off!"
            self.appendMessage(message)
      
def main():
    root = tk.Tk()
    root.title("Smart Home Control Panel")

    light5 = SmartLight(1, "off", 100)
    thermostat5 = Thermostat(1, "off", 20)
    camera5 = SecurityCamera(1, "off", "OFF")

    SmartHomeGUI(root, light5, thermostat5, camera5)

    root.mainloop()

if __name__ == "__main__":
    main()