from scripts.modules.utils.hex_to_binary import hex_to_binary


def test_hex_to_binary():
    orig_number = 789
    hex_number = hex(orig_number)[2:]
    binary_number = hex_to_binary(hex_number)

    assert int(binary_number, 2) == orig_number
