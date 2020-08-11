from behaviour import BuiltInChipBehaviour, CustomChipBehaviour, BehaviourInterface


class Chip:

    def __init__(self, identifier, **kwargs):
        self.identifier = identifier

        self.properties = kwargs

        self.io_behaviour = BehaviourInterface()

    def set_behaviour(self, obj):
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
