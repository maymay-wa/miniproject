from abc import ABC, abstractmethod

# Base class for all neurons
class GeneralNeuron:
    def __init__(self, firing_rate=0.0):
        self.firing_rate = firing_rate

    @abstractmethod
    def activate(self, stimulus_strength):
        # Generic activation based on stimulus strength
        self.firing_rate = stimulus_strength * 0.1
        return f"Firing rate set to {self.firing_rate} Hz"

# Sensory neuron base class
class SensoryNeuron(GeneralNeuron):
    def __init__(self, firing_rate=0.0, receptor_type=""):
        super().__init__(firing_rate)
        self.receptor_type = receptor_type

    @abstractmethod
    def sense_stimulus(self, stimulus):
        return f"Sensing {self.receptor_type} stimulus: {stimulus}"

# Motor neuron base class
class MotorNeuron(GeneralNeuron):
    def __init__(self, firing_rate=0.0, target_muscle=""):
        super().__init__(firing_rate)
        self.target_muscle = target_muscle

    @abstractmethod
    def control_muscle(self):
        return f"Controlling {self.target_muscle} with firing rate {self.firing_rate} Hz"

# Specific sensory neuron: Photoreceptor
class Photoreceptor(SensoryNeuron):
    def __init__(self, firing_rate=0.0):
        super().__init__(firing_rate, receptor_type="light")

    def detect_light(self, light_intensity):
        self.firing_rate = light_intensity * 0.2
        return f"Photoreceptor activated: Firing rate {self.firing_rate} Hz"

# Specific sensory neuron: Mechanoreceptor
class Mechanoreceptor(SensoryNeuron):
    def __init__(self, firing_rate=0.0):
        super().__init__(firing_rate, receptor_type="pressure")

    def detect_pressure(self, pressure_level):
        self.firing_rate = pressure_level * 0.3
        return f"Mechanoreceptor activated: Firing rate {self.firing_rate} Hz"

# Specific motor neuron: Alpha Motor Neuron
class AlphaMotorNeuron(MotorNeuron):
    def __init__(self, firing_rate=0.0):
        super().__init__(firing_rate, target_muscle="skeletal muscle")

    def skeletal_muscle_control(self):
        return f"Alpha Motor Neuron controlling skeletal muscle: Contraction strength proportional to {self.firing_rate} Hz, and is fast with rapid connections"

# Specific motor neuron: Gamma Motor Neuron
class GammaMotorNeuron(MotorNeuron):
    def __init__(self, firing_rate=0.0):
        super().__init__(firing_rate, target_muscle="muscle spindle")

    def muscle_spindle_control(self):
        return f"Gamma Motor Neuron adjusting muscle tone: Response level proportional to {self.firing_rate} Hz, is slow with slow connections"