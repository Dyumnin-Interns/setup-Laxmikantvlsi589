module dut_test(
    input wire a,
    input wire b,
    output wire y
);

    dut dut_inst (
        .a(a),
        .b(b),
        .y(y)
    );

    initial begin
        $dumpfile("tests/xor.vcd");
        $dumpvars(0, dut_test);
    end

endmodule

