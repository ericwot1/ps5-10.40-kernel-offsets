# PS5 FW 10.40 – Kernel Offsets, Syscalls & ROP Gadgets

---

## 1. Syscalls

### `recv`
**Description**: Receives data from a network socket. 
**ID** : 29  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `accept`
**Description**: Accepts a new incoming connection (server).
**ID** : 30  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `socket`
**Description**: Creates a new network socket.
**ID** : 97  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `bind`
**Description**: Associates a socket with an IP address and port.  
**ID** : 104  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `listen`
**Description** : Makes a socket listen for incoming connections.  
**ID** : 106  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `send`
**Description** : Sends data via a network socket.
**ID** : 133  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

---

## 2. ROP Gadgets

### `pop rdi ; ret
**Description** : Loads a value into `RDI`.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `pop rsi ; ret`
**Description** : Loads a value into `RSI`.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `pop rax ; ret`
**Description** : Loads a value into `RAX`.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `mov [rdi], rsi ; ret`
**Description** : Writes the value of `RSI` to the address pointed to by `RDI`.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `syscall`
**Description** : Calls a kernel syscall with the current registers. 
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `leave ; ret`
**Description** : Gadget pivot (stack pivot).  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

---

## 3. Kernel Offsets

### `allproc`
**Description** : Linked list of processes. 
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `rootvnode`
**Description** : Root of the file system.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `pmap_store`
**Description** : Memory paging management. 
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `kernel_pmap_store`
**Description** : Main pointer to pmap kernel.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `ucred`
**Description** : UID/GID user.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `security_flags`
**Description** : Security related flags.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

---

# Notes

- Base kernel : **0xFFFFFFFF80000000**  
- Remplace les `XXXXXX` par tes offsets trouvés dans IDA.  
- Vérifiés en Hex View et Disassembly.  

