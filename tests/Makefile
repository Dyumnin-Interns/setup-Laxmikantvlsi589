SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/../hdl/dut.v

all: xor

xor:
	rm -rf sim_build
	$(MAKE) sim MODULE=dut_test TOPLEVEL=dut

include $(shell cocotb-config --makefiles)/Makefile.sim
