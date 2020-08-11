import xml.etree.ElementTree as ET

tree = ET.parse('chip_collection.xml')
root = tree.getroot()


class BehaviourInterface():

    @staticmethod
    def get_chip_element(identifier): pass

    def get_input_pins(self): pass

    def get_output_pins(self): pass


class CustomChipBehaviour(BehaviourInterface):
    
    def __init__(self, identifier):
        pass

    @staticmethod
    def get_chip_element(identifier):
        try:
            tree = ET.parse('{}.xml'.format(identifier))
            root = tree.getroot()
            return [items for items in root]
        except FileNotFoundError as e:
            print(e)


class BuiltInChipBehaviour(BehaviourInterface):

    def __init__(self, identifier):
        self.element = self.get_chip_element(identifier)
        self.connection_panel = self.element.find("ConnectionPanel")

    @staticmethod
    def get_chip_element(identifier):
        for item in root.iter("Item"):
            if item.attrib["identifier"] == identifier:
                return item

    def get_input_pins(self):
        return [pin for pin in self.connection_panel.findall("input")]

    def get_output_pins(self):
        return [pin for pin in self.connection_panel.findall("output")]


class Wire:

    def __init__(self, id, hidden_in_game=True, noninteractable=True):
        self.id = id
        self.hidden_in_game = hidden_in_game
        self.noninteractable = noninteractable

        self._input_end = []
        self._output_end = []

    @property
    def input_end(self):
        return self._input_end

    @input_end.setter
    def input_end(self, inputs):
        self._input_end = inputs

    @property
    def output_end(self):
        return self._output_end

    @output_end.setter
    def output_end(self, outputs):
        self._output_end = outputs


if __name__ == "__main__":
    c = BuiltInChipBehaviour("andcomponent")
    print(c.get_chip_element("andcomponent").attrib)