import os

dir_path = r'C:\Users\User\Documents\KiCAD_Library_AS\Footprints\temp.pretty'
for filename in os.listdir(dir_path):
    if filename.endswith('.kicad_mod'):
        file_path = os.path.join(dir_path, filename)
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        
        # Replace 'module' with 'footprint' for modern KiCad compatibility
        # And remove the 'easyeda2kicad:' prefix if it exists
        content = content.replace('(module easyeda2kicad:', '(footprint "')
        if '(module ' in content and 'easyeda2kicad:' not in content:
             content = content.replace('(module ', '(footprint "')
        
        # Close the quote if we started one
        if '(footprint "' in content and ' (layer' in content:
            # Find the space before (layer
            idx = content.find(' (layer')
            header = content[:idx]
            if '"' in header and header.count('"') == 1:
                content = header + '"' + content[idx:]

        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
