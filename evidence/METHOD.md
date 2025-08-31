# Méthodologie d’extraction et de confirmation des offsets PS5 FW 10.40

Ce document décrit comment les offsets et gadgets ROP ont été identifiés et confirmés pour le firmware PlayStation 5 version 10.40. 

## Outils utilisés
- Dump du kernel 10.40
- IDA Pro 9.1 / Ghidra
- Scripts Python personnalisés
- Bibliothèque Capstone

## Procédure
1. Chargement du dump kernel dans IDA et Ghidra.
2. Analyse automatique du désassemblage.
3. Recherche manuelle et automatisée de gadgets classiques (leave; ret, pop rdi; ret, pop rsi; ret, pop rax; ret, mov [rax], edx; ret).
4. Vérification manuelle de chaque adresse dans IDA.
5. Enregistrement des résultats confirmés dans ps5_fw1040_gadgets_offsets.csv.

## Preuves prévues
- Captures d’écran (dossier evidence/screenshots).
- Fichier ps5_fw1040_gadgets_offsets.csv.
- Script de vérification (evidence/scripts/verify_offsets.py).
- Logs d’exécution (evidence/logs/).

## Conclusion
Les résultats publiés sont obtenus manuellement et vérifiables. Ils concernent le **kernel PS5 FW 10.40** et non le userland des jeux.
