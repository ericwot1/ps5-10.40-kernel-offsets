# PS5 FW 10.40 – Kernel Offsets, Syscalls & ROP Gadgets

---

## 1. Syscalls

### `recv`
**Description** : Reçoit des données depuis un socket réseau.  
**ID** : 29  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `accept`
**Description** : Accepte une nouvelle connexion entrante (serveur).  
**ID** : 30  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `socket`
**Description** : Crée un nouveau socket réseau.  
**ID** : 97  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `bind`
**Description** : Associe un socket à une adresse IP et un port.  
**ID** : 104  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `listen`
**Description** : Met un socket en écoute pour accepter des connexions entrantes.  
**ID** : 106  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `send`
**Description** : Envoie des données via un socket réseau.  
**ID** : 133  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

---

## 2. ROP Gadgets

### `pop rdi ; ret`
**Description** : Charge une valeur dans `RDI`.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `pop rsi ; ret`
**Description** : Charge une valeur dans `RSI`.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `pop rax ; ret`
**Description** : Charge une valeur dans `RAX`.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `mov [rdi], rsi ; ret`
**Description** : Écrit la valeur de `RSI` à l’adresse pointée par `RDI`.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `syscall`
**Description** : Appelle un syscall du kernel avec les registres courants.  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

### `leave ; ret`
**Description** : Gadget pivot (stack pivot).  
**Adresse** : `0xFFFFFFFF80XXXXXX`  
**Status** :  Confirmed  

---

## 3. Kernel Offsets

### `allproc`
**Description** : Liste chaînée des processus.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `rootvnode`
**Description** : Racine du système de fichiers.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `pmap_store`
**Description** : Gestion pagination mémoire.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `kernel_pmap_store`
**Description** : Pointeur principal vers pmap kernel.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `ucred`
**Description** : UID/GID utilisateur.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

### `security_flags`
**Description** : Flags liés à la sécurité.  
**Adresse** : `0xFFFFFFFF82XXXXXX`  
**Status** :  Confirmed  

---

# Notes

- Base kernel : **0xFFFFFFFF80000000**  
- Remplace les `XXXXXX` par tes offsets trouvés dans IDA.  
- Vérifiés en Hex View et Disassembly.  

