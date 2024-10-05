import argparse

from caches import *

import m5
from m5.objects import *

parser = argparse.ArgumentParser(
    description="A simple system with 2-level cache."
)
# parser.add_argument("binary", default="", nargs="?", type=str,
#                     help="Path to the binary to execute.")
parser.add_argument(
    "--l1i_size", help=f"L1 instruction cache size. Default: 16kB."
)
parser.add_argument(
    "--l1d_size", help="L1 data cache size. Default: Default: 64kB."
)
parser.add_argument("--l2_size", help="L2 cache size. Default: 256kB.")

options = parser.parse_args()

# system代表模拟系统，是zsim仿真所有对象的父对象
system = System()

# 设置时钟域，确定频率和电压
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = "1GHz"
system.clk_domain.voltage_domain = VoltageDomain()

# 创建timming模式的mem，timming mode？
system.mem_mode = "timing"
system.mem_ranges = [AddrRange("512MB")]

# 创建cpu，时序cpu，是顺序的意思
system.cpu = X86TimingSimpleCPU()
# RiscvTimingSimpleCPU可以创建riscV的cpu

# 创建缓存
system.cpu.icache = L1ICache(options)
system.cpu.dcache = L1DCache(options)

# 连接L1的cpu port
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)

# 创建l2bus
system.l2bus = L2XBar()

# 连接L1的bus port
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)

# 创建L2
system.l2cache = L2Cache()

# 连接L2的cpu side port
system.l2cache.connectCPUSideBus(system.l2bus)

# 内存总线
system.membus = SystemXBar()

# 连接L2的mem side port
system.l2cache.connectMemSideBus(system.membus)


system.cpu.createInterruptController()
system.cpu.interrupts[0].pio = system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports

system.system_port = system.membus.cpu_side_ports

system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.dram.range = system.mem_ranges[0]
system.mem_ctrl.port = system.membus.mem_side_ports

binary = (
    "/data/yijia/simulator/gem5/tests/test-progs/hello/bin/x86/linux/hello"
)

# for gem5 V21 and beyond
system.workload = SEWorkload.init_compatible(binary)

process = Process()
process.cmd = [binary]
system.cpu.workload = process
system.cpu.createThreads()

root = Root(full_system=False, system=system)
m5.instantiate()

print("Beginning simulation!")
exit_event = m5.simulate()

print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")
