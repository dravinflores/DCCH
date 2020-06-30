def push_data_to_shift_register(byte_string, data_pin, write_pin):
    # Go bit by bit.
    for bit in byte_string:
        pin = bit
        write_pin = True
        write_pin = False


def sync_to_manifolds(sync_pin):
    sync_pin = True
    sync_pin = False


def clear_shift_registers(clear_pin):
    clear_pin = False
    clear_pin = True


def main():
    # Simplified Python program to illustrate the usage of the PCB.

    # The initial states of the pins.
    DATA_IN = False
    SYNC = False
    WRITE = False
    CLEAR = True

    # Clear all shift registers.
    CLEAR = False
    CLEAR = True

    # Labels, for convenience.
    data_in_label = [
        # Tubes 8 & 7
        'OFF', '8B', '8A', 'ENABLE TUBE 8', '7B', '7A', 'ENABLE TUBE 7', 'OFF'

        # Tubes 6 & 5
        'OFF', '6B', '6A', 'ENABLE TUBE 6', '5B', '5A', 'ENABLE TUBE 5', 'OFF'

        # Tubes 4 & 3
        'OFF', '4B', '4A', 'ENABLE TUBE 4', '3B', '3A', 'ENABLE TUBE 3', 'OFF'

        # Tubes 2 & 1
        'OFF', '2B', '2A', 'ENABLE TUBE 2', '1B', '1A', 'ENABLE TUBE 1', 'OFF'
    ]

    # We want to connect the first two tubes to the system. This is the data
    # string that will do that. Connecting tubes 1 and 2.
    data_string = [
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False,
        False, False, True, True, False, True, True, False,
    ]
    push_data_to_shift_register(data_string, DATA_IN, WRITE)
    sync_to_manifolds(SYNC)
    clear_shift_registers(CLEAR)

    # To connect the next two tubes to the system, we will use the following
    # data string. Connecting tubes 3 and 4.
    data_string = [
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False,
        False, False, True, True, False, True, True, False,
        False, False, False, False, False, False, False, False
    ]
    push_data_to_shift_register(data_string, DATA_IN, WRITE)
    sync_to_manifolds(SYNC)
    clear_shift_registers(CLEAR)

    # Connecting tubes 5 and 6.
    data_string = [
        False, False, False, False, False, False, False, False,
        False, False, True, True, False, True, True, False,
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False
    ]
    push_data_to_shift_register(data_string, DATA_IN, WRITE)
    sync_to_manifolds(SYNC)
    clear_shift_registers(CLEAR)

    # Connecting tubes 7 and 8.
    data_string = [
        False, False, True, True, False, True, True, False,
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False
    ]
    push_data_to_shift_register(data_string, DATA_IN, WRITE)
    sync_to_manifolds(SYNC)
    clear_shift_registers(CLEAR)

    
    # To disconnect a single tube from the system, we can use either of the two
    # data strings. You would simply just have to pad this data string with
    # zeros, depending on where the tube was.
    data_string_even_tube = [
        False, True, False, True, False, False, False, False
    ]

    data_string_odd_tube = [
        False, False, False, False, True, False, True, False
    ]

    # For instance, here is the padded data string to disconnect the fifth tube
    # from the system.
    data_string = [
        # Tubes 8 & 7
        False, False, False, False, False, False, False, False,

        # Tubes 6 & 5. Notice how I just placed the odd data string here.
        False, False, False, False, True, False, True, False

        # Tubes 4 & 3
        False, False, False, False, False, False, False, False,

        # Tubes 2 & 1
        False, False, False, False, False, False, False, False
    ]
    push_data_to_shift_register(data_string, DATA_IN, WRITE)
    sync_to_manifolds(SYNC)
    clear_shift_registers(CLEAR)

    # And that's about it.


# Call main().
main()