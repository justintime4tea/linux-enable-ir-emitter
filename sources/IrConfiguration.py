from Driver import Driver

# old version, ensure compatibility with 3.3.0
class IrConfiguration(Driver):
    def __init__(self, control, unit, selector, device):
        super().__init__(control, unit, selector, device)
