import os

dir_path = r'C:\Users\User\Documents\KiCAD_Library_AS\Footprints\AS.pretty'
for filename in os.listdir(dir_path):
    if filename.endswith('.kicad_mod'):
        file_path = os.path.join(dir_path, filename)
        try:
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                content = f.read()
            
            # Replace 'module' with 'footprint' for modern KiCad compatibility
            if '(module' in content:
                content = content.replace('(module easyeda2kicad:', '(footprint "')
                content = content.replace('(module ', '(footprint "')
                
                # Ensure the opening name is quoted and the path variable is set
                idx = content.find(' (layer')
                if idx != -1:
                    header = content[:idx]
                    if header.count('"') == 1:
                        content = header + '"' + content[idx:]
                
                # Patch 3D path if not already patched
                content = content.replace('(model "Symbols/AS.3dshapes/', '(model "${KICAD_AS_3D}/AS.3dshapes/')

                with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(content)
        except Exception as e:
            print(f"Error fixing {filename}: {e}")
