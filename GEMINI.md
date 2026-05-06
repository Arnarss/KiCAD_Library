# KiCAD_Library_AS - Project Log & Instructions

This file serves as a persistent "memory" for Gemini CLI. When you start a new session in this folder, Gemini reads this file to understand the project rules.

## 🎯 MANDATE FOR FUTURE SESSIONS
When the user provides an LCSC Part ID (e.g., "C12345"):
1. **Download:** Use `python -m easyeda2kicad --lcsc_id <ID> --full --output Symbols/AS.kicad_sym --overwrite`.
2. **Organize:** 
   - Move `.kicad_mod` files from `Symbols/AS.pretty/` to `Footprints/AS.pretty/`.
   - Move `.step`/`.wrl` files from `Symbols/AS.3dshapes/` to `3D_Models/AS.3dshapes/`.
   - Delete the temporary `Symbols/AS.pretty` and `Symbols/AS.3dshapes` folders.
3. **Patch:** Automatically update the footprint's 3D model path to use `${KICAD_AS_3D}/AS.3dshapes/` and ensure the file format is modern `(footprint ...)`.
4. **Log:** Update the "Components Downloaded" list in this file.

## 📂 Library Structure
- **Symbols/**: `AS.kicad_sym` (Nickname: `AS`)
- **Footprints/AS.pretty/**: `.kicad_mod` files (Nickname: `AS`)
- **3D_Models/AS.3dshapes/**: `.step` and `.wrl` files (Variable: `KICAD_AS_3D`)

## ⚙️ KiCad Configuration
1. **Path Variable:** `KICAD_AS_3D` -> `C:\Users\User\Documents\KiCAD_Library_AS\3D_Models`
2. **Symbol Lib:** `Symbols/AS.kicad_sym` (Nickname: `AS`)
3. **Footprint Lib:** `Footprints/AS.pretty` (Nickname: `AS`)

## 📦 Components Downloaded (LCSC IDs)
- **C5438434**: NORA-B106-00B (Bluetooth Module)
- **C7501206**: NPM1300-QEAA-R7 (PMIC)
- **C97521**: W25Q128JVSIQTR (Flash Memory)
- **C526225**: EVQPUK02K (Tactile Switch)
- **C74512**: AT42QT1010-TSHR (Touch Sensor)
- **C46898862**: LSM6DSV80XTR (IMU)
- **C2835313**: TYPEC-302-BRP16SC16 (USB-C)
- **C2827693**: USBLC6-2P6 (ESD Protection)
- **C425927**: DRV2605LDGST (Haptic Driver)
- **C5349953**: XL-1010RGBC-WS2812B (RGB LED)
- **C70377**: CR2032-BS-6-1 (Battery Holder)
