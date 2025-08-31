# find_gadgets.py — IDAPython script for PS5 FW 10.40
# Scan for common ROP gadgets (pop, mov, syscall)

import ida_search
import idc

patterns = {
    "pop rdi ; ret": b"\x5F\xC3",
    "pop rsi ; ret": b"\x5E\xC3",
    "pop rax ; ret": b"\x58\xC3",
    "mov [rdi], rsi ; ret": b"\x48\x89\x37\xC3",
    "leave ; ret": b"\xC9\xC3",
    "syscall": b"\x0F\x05",
}

print("Starting gadget scan...")
for name, pat in patterns.items():
    ea = ida_search.find_binary(0, idc.BADADDR, pat.hex(" "), 16, ida_search.SEARCH_DOWN)
    while ea != idc.BADADDR:
        print(f"Found {name} at 0x{ea:X}")
        ea = ida_search.find_binary(ea + 1, idc.BADADDR, pat.hex(" "), 16, ida_search.SEARCH_DOWN)

print("Scan completed.")
