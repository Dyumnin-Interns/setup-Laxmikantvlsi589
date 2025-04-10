SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/../hdl/dut.v
TOPLEVEL = dut
MODULE = dut_test

WAVES ?= 1
export VCD_NAME ?= xor_waveform

include $(shell cocotb-config --makefiles)/Makefile.sim

