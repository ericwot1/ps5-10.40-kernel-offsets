HEAD
# PS5 kernel 10.40 Offest Rop ....

## Extra Syscalls (useful in exploits)

| Syscall     | Number | Status   |
|-------------|--------|----------|
| connect     | 98     | Confirmed |
| shutdown    | 134    | Confirmed |
| getpeername | 31     | Confirmed |
| getsockname | 32     | Confirmed |
| setsockopt  | 105    | Confirmed |
| getsockopt  | 118    | Confirmed |
| open        | 5      | Confirmed |
| read        | 3      | Confirmed |
| write       | 4      | Confirmed |
| mmap        | 197    | Confirmed |
| mprotect    | 74     | Confirmed |
| munmap      | 73     | Confirmed |
| getpid      | 20     | Confirmed |
| kill        | 37     | Confirmed |
| ptrace      | 26     | Confirmed |
 9548cf6 (Update KERNEL10.40_offsets.md with extra syscalls (connect, mmap, ptrace, etc.))

## Stack Pivot Gadgets (stack control)
| Gadget      | Validated Address(es)                  | Status   |
|-------------|----------------------------------------|----------|
| leave ; ret | 0x1431e8c, 0x2a59a6, 0x3090fb6          | Confirmed |
| retn        | 0x1c525f, 0x25c2204, 0x2e09814          | Confirmed |

## POP Gadgets (register control)
| Gadget       | Validated Address(es)                  | Status   |
|--------------|----------------------------------------|----------|
| pop rdi ; ret | 0x401bcd, 0xce22e, 0x4951da…          | Confirmed |
| pop rsi ; ret | 0x8744c2, 0x13e215c, 0x8e93ab…        | Confirmed |
| pop rax ; ret | 0x10fdf65, 0xceae5e, 0x8910dd…        | Confirmed |

## Write Gadgets (memory write)
| Gadget          | Address       | Usage / Notes              | Status   |
|-----------------|---------------|----------------------------|----------|
| mov [rax], edx ; ret | 0x17df1   | Patch cr_uid = 0           | Critical |
| mov [rax], ecx ; ret | 0x2d274   | Patch cr_uid = 0           | Critical |
| mov [rax], bl ; ret  | 0x46e0b   | 1-byte write (limited use) | Confirmed |
| mov [rdi], rsi ; ret | (scanned binaries) | Generic 64-bit write | Confirmed |
| mov [rax], rdx ; ret | (scanned binaries) | Generic 64-bit write | Confirmed |

## Syscall Gadgets
| Gadget        | Validated Address(es)                  | Status   |
|---------------|----------------------------------------|----------|
| syscall ; ret | 0x17a6503, 0x1b03244                   | Confirmed |

## Kernel Offsets (core structures)
| Structure | Field     | Offset | Status   |
|-----------|-----------|--------|----------|
| proc      | p_pid     | 0xBC   | Confirmed |
| proc      | p_ucred   | 0x4C   | Confirmed |
| proc      | p_vmspace | 0x200  | Confirmed |
| ucred     | cr_uid    | 0x04   | Confirmed |
| ucred     | cr_ruid   | 0x08   | Confirmed |
| ucred     | cr_svuid  | 0x0C   | Confirmed |
| ucred     | cr_groups | 0x14   | Confirmed |

## Vulnerable Handlers (IOCTL triggers)
| Instruction | Immediate Value | Status     |
|-------------|-----------------|------------|
| cmp eax, imm | 0x63F9510D     | Vulnerable |
| cmp eax, imm | 0xE9E06708     | Vulnerable |
| and eax, imm | 0xBE1B09B6     | Vulnerable |
| test eax, imm| 0x4F5DDF91     | Vulnerable |

## Network Syscalls (confirmed in entry_171199)
| Syscall | Number | Approx. Hits | Status   |
|---------|--------|--------------|----------|
| recv    | 29     | ~16,825      | Confirmed |
| accept  | 30     | ~17,000      | Confirmed |
| socket  | 97     | ~15,087      | Confirmed |
| bind    | 104    | ~14,885      | Confirmed |
| listen  | 106    | ~17,067      | Confirmed |
| send    | 133    | ~15,763      | Confirmed |
