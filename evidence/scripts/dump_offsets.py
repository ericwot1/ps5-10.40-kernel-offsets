# dump_offsets.py — IDAPython script for PS5 FW 10.40
# Locate kernel structures of interest

targets = [
    "allproc",
    "rootvnode",
    "pmap_store",
    "kernel_pmap_store",
    "ucred",
    "security_flags"
]

print("Scanning for kernel offsets...")
for t in targets:
    ea = idc.get_name_ea_simple(t)
    if ea != idc.BADADDR:
        print(f"{t} → 0x{ea:X}")
    else:
        print(f"{t} not found.")

print("Offset dump completed.")
