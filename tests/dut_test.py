import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def dut_test(dut):
    a_values = (0, 0, 1, 1)
    b_values = (0, 1, 0, 1)
    expected_y = (0, 1, 1, 0)

    for i in range(4):
        dut.a.value = a_values[i]
        dut.b.value = b_values[i]
        await Timer(1, 'ns')
        assert dut.y.value == expected_y[i], f"XOR failed at iteration {i}: {a_values[i]} ^ {b_values[i]} != {dut.y.value}"
