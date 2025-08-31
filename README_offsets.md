# PS5 FW 10.40 Kernel Offsets & ROP Gadgets

Ce dépôt contient des résultats confirmés pour le firmware PlayStation 5 version 10.40, côté **kernel**.  
Les gadgets et offsets inclus concernent la recherche bas niveau (kernel ROP, syscalls, structures comme allproc et ucred).  

## Contenu
- ps5_fw1040_gadgets_offsets.csv : offsets et gadgets confirmés
- evidence/ : preuves et scripts de vérification
  - METHOD.md : explications de la méthodologie
  - screenshots/ : captures d’écran (à venir)
  - logs/ : sorties de scripts de vérification
  - scripts/ : scripts Python de vérification

## Statut
Les résultats sont confirmés et testés sur dump réel 10.40.  
Ils ne concernent pas le userland des jeux ni les loaders comme `remote_lua_loader`.  

## Lien
https://github.com/ericwot1/ps5-10.40-kernel-offsets
