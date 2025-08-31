# find_syscalls.py — IDAPython script for PS5 FW 10.40
# Locate syscalls of interest (recv, accept, socket, bind, listen, send)

import idautils
import idc

syscalls = {
    29: "recv",
    30: "accept",
    97: "socket",
    104: "bind",
    106: "listen",
    133: "send"
}

print("Scanning for syscalls...")
for ea in idautils.Functions():
    name = idc.get_func_name(ea)
    for num, syscall in syscalls.items():
        if syscall in name.lower():
            print(f"Found syscall {syscall} (ID {num}) at 0x{ea:X}")

print("Syscall scan completed.")
