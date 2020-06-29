# This is just so that we can abstract away the idea of a pin.
class pin:
    def __init__(self, name, state):
        self.name = name
        self.state = state

    def __str__(self):
        return f"{self.name} is set to {self.state}"

    def set(self, state):
        self.state = state


class register:
    def __init__(self):
        self.state = list()

    def push(self, bit):
        self.state.append(bit)

    def print(self):
        for bit in self.state:
            print(int(bit), end='')
        print()

    def clear(self):
        self.state = list()


def main():
    # Here I am defining the pins on the PCB itself. These are the default 
    # states. I will opt to use True/False instead of HIGH/LOW or 0/1.
    DATA_IN = pin("DATA_IN", False)
    SYNC = pin("SYNC", False)
    WRITE = pin("WRITE", False)
    CLEAR = pin("CLEAR", True)

    # We're going to pretend this is the shift register.
    SHIFT = register()

    # First, we want to clear all the data in the shift registers. This is an
    # active low signal, meaning to clear it must first be set to False. If it
    # is not set back to True, then it will constantly clear the register.
    CLEAR.set(False)
    CLEAR.set(True)

    # I want to enable the first two tubes. This will have the 8 bit pattern 
    # 01101100, which will be passed to the DATA_IN pin. In Python, we can
    # represent the bit string as a list, and then iterate through using a
    # for loop.
    byte_str = [False, True, True, False, True, True, False, False]

    for bit in byte_str:
        DATA_IN.set(bit)
        WRITE.set(True)
        WRITE.set(False)

        # In this case, the bit has been pushed to the shift register. So
        # internally, the wiring would push this bit into the shift register
        # itself, so we wouldn't necessarily see this step.
        SHIFT.push(bit)

    # Once we've pushed in all the bits sequentially, it is stored in the
    # register. Now we need to push it to the output.
    SYNC.set(True)
    SYNC.set(False)
    print("Shift Register for tubes 1 & 2: ", end='')
    SHIFT.print()


    # So we've enabled the first two tubes. Now we will need to enable the next
    # two, without disturbing the first two tubes. So we're going to
    # get the same string, just with a few ending zeros. Here the rows
    # correspond to bytes, or rather the first and second shift registers.
    byte_str = [
        False, False, False, False, False, False, False, False,
        False, True, True, False, True, True, False, False,
    ]

    # Don't forget to clear the shift register.
    CLEAR.set(False)
    CLEAR.set(True)
    SHIFT.clear()

    for bit in byte_str:
        DATA_IN.set(bit)
        WRITE.set(True)
        WRITE.set(False)

        # Once again, this would be automatically done for us, in the actual
        # circuit.
        SHIFT.push(bit)

    # Now that the shift register has all the data, we just need to push it
    # to the output.
    SYNC.set(True)
    SYNC.set(False)
    print("Shift Register for tubes 3 & 4: ", end='')
    SHIFT.print()


    # Now for tubes 5 and 6.
    byte_str = [
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False,
        False, True, True, False, True, True, False, False,
    ]

    # Don't forget to clear the shift register.
    CLEAR.set(False)
    CLEAR.set(True)
    SHIFT.clear()

    for bit in byte_str:
        DATA_IN.set(bit)
        WRITE.set(True)
        WRITE.set(False)

        # Once again, this would be automatically done for us, in the actual
        # circuit.
        SHIFT.push(bit)

    # Now that the shift register has all the data, we just need to push it
    # to the output.
    SYNC.set(True)
    SYNC.set(False)
    print("Shift Register for tubes 5 & 6: ", end='')
    SHIFT.print()


    # Lastly, tubes 7 and 8.
    byte_str = [
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False,
        False, True, True, False, True, True, False, False,
    ]

    # Don't forget to clear the shift register.
    CLEAR.set(False)
    CLEAR.set(True)
    SHIFT.clear()

    for bit in byte_str:
        DATA_IN.set(bit)
        WRITE.set(True)
        WRITE.set(False)

        # Once again, this would be automatically done for us, in the actual
        # circuit.
        SHIFT.push(bit)

    # Now that the shift register has all the data, we just need to push it
    # to the output.
    SYNC.set(True)
    SYNC.set(False)
    print("Shift Register for tubes 7 & 8: ", end='')
    SHIFT.print()


    # One final clear.
    CLEAR.set(False)
    CLEAR.set(True)
    SHIFT.clear()

    
    # Of course this process would go on and on, for however many tubes are
    # connected to the circuit. In this manner, I would expect there are a few
    # subroutines that can be made, although I am unsure of how to do this in
    # LabView.

    # To disengage an odd tube from the system, this is the bit string:
    byte_str = [False, True, False, True, False, False, False, False]

    # To disengage an even tube from the system, this is the bit string:
    byte_str = [False, False, False, False, True, False, True, False]

    # Of course the numbering goes Tube 1, Tube 2, ... , Tube 8.

main()