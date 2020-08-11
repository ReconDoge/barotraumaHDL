from behaviour import BuiltInChipBehaviour, CustomChipBehaviour, BehaviourInterface

'''A library of chip objects that includes the base chip class, a built in chip class and would probably include
a custom chip class that would get implemented in the future.

Built in chips are existing logic components in the game that are described within <item> tags in the chip_collection.xml
file. There would also be a user defined chip that is made up of built-in chips created using the HDL. However, it has
not been implemented yet'''


class Chip:
    '''basic chip class that has an identifier and a bunch of properties that would need to correspond to the
    attributes in the XML file'''
    def __init__(self, identifier, **kwargs):
        self.identifier = identifier

        self.properties = kwargs

        self.io_behaviour = BehaviourInterface()

    def set_behaviour(self, obj):
        #sets the chip's behaviour to either a built-in chip or a custom chip
        self.io_behaviour = obj

    def get_behaviour(self):
        return self.io_behaviour

    @property
    def input_pins(self):
        return self.io_behaviour.get_input_pins()

    @property
    def output_pins(self):
        return self.io_behaviour.get_output_pins()


class BuiltInChip(Chip):

    def __init__(self, identifier, **kwargs):
        super().__init__(identifier, **kwargs)

        self.set_behaviour(BuiltInChipBehaviour(self.identifier))


class And(BuiltInChip):
    '''Not sure if this approach is a good one because it would require a massive number of classes
    to implement all of the built-in chips.'''
    _identifier = "andcomponent"
    def __init__(self, **kwargs):
        super().__init__(self._identifier, **kwargs)


class Or(BuiltInChip):

    _identifier = "orcomponent"
    def __init__(self, **kwargs):
        super().__init__(self._identifier, **kwargs)


if __name__ == "__main__":
    c = And(id=3, noneinterfactable=True)
    print(c.properties)
