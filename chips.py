import xml.etree.ElementTree as ET

tree = ET.parse('chip_collection.xml')
root = tree.getroot()
'''test'''

class IOBehaviourInterface():

    @staticmethod
    def get_chip_element(identifier): pass

    def get_input_pins(self): pass

    def get_output_pins(self): pass


#class CustomChipBehaviour(IOBehaviourInterface):
#    pass


class BuiltInChipBehaviour(IOBehaviourInterface):

    def __init__(self, identifier):
        self.element = self.get_chip_element(identifier)
        self.connection_panel = self.element.find("ConnectionPanel")

    @staticmethod
    def get_chip_element(identifier):
        for item in root.iter("Item"):
            if item.attrib["identifier"] == identifier:
                return item

    def get_input_pins(self):
        return [pin.get("name") for pin in self.connection_panel.findall("input")]

    def get_output_pins(self):
        return [pin.get("name") for pin in self.connection_panel.findall("output")]


class Chip:

    def __init__(self, identifier, noninteractable=True, hidden_in_game=True):
        self.identifier = identifier
        self.noninteractable = noninteractable
        self.hidden_in_game = hidden_in_game
        self.attributes = None
        self.input_pins = None
        self.output_pins = None

        self.io_behaviour = IOBehaviourInterface()

    def set_behaviour(self, obj):
        self.io_behaviour = obj

    def get_behaviour(self):
        return self.io_behaviour

    def get_input_pins(self):
        return self.io_behaviour.get_input_pins()

    def get_output_pins(self):
        return self.io_behaviour.get_output_pins()


class BuiltInChip(Chip):

    def __init__(self, identifier, noninteractable=True, hidden_in_game=True):
        super().__init__(identifier, noninteractable, hidden_in_game)

        self.set_behaviour(BuiltInChipBehaviour(self.identifier))

        #self.attributes = self.io_behaviour.get_chip_element(self.identifier).attrib()



c = BuiltInChip("andcomponent")
print(c.get_input_pins())
print(c.get_output_pins())
