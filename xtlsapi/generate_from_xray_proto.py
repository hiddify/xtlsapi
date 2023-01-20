#https://www.plcnext-community.net/makersblog/grpc-python-read-and-write-process-data/
import glob
import os
from pathlib import Path

package_name="xtlsapi.xray_api"
out="/opt/xtlsapi/xtlsapi/xray_api/"
#out="xtlsapi/xray_api"
xray_src="/opt/Xray-core/"
# create the output directory
Path(out).mkdir(parents=True, exist_ok=True)



grpc_command_base = f'cd {xray_src}; python3 -m grpc_tools.protoc -I ./ --python_out={out} --grpc_python_out={out} '
protoc_command_base = f'cd {xray_src}; protoc --python_out={out} '
import_paths = set()

# generate the *_pb2.py and *_pb2_grpc.py files
for filename in glob.iglob(f'{xray_src}/**/*.proto', recursive=True):
    print(filename)
    if filename.endswith('.proto'):
        
        # store the import path
        path_parts = filename.replace(xray_src,"./").split(os.sep)
        import_paths.add('.'.join(path_parts[1:-1]))

        grpc_command = ''.join([grpc_command_base, os.path.join('.', filename.replace(xray_src,""))])
        protoc_command = ''.join([protoc_command_base, os.path.join('.', filename.replace(xray_src,""))])
        print(grpc_command)
        stream = os.popen(grpc_command)
        output = stream.read()
        if output != '':
            print(''.join(['error/info for file ', filename, ' - ', output]))
        stream = os.popen(protoc_command)
        output = stream.read()
        if output != '':
            print(''.join(['protoc error/info for file ', filename, ' - ', output]))

# get the python files in the base directory
base_pys = set()

for (dirpath, dirnames, filenames) in os.walk(f'{out}'):
    for f in filenames:
        base_pys.add(f.split('.py')[0])
    break

# reformat the stored paths to adapt the import statements
try:
    import_paths.remove('')
except:
    pass

import_paths = list(import_paths)
import_paths.sort(key=len)
import_paths.reverse()

# adapt the imports
for filename in glob.iglob(f'{out}/**', recursive=True):
#    print(filename)
    if filename.endswith('.py'):

        new_lines = []

        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('from'):
                    for import_path in import_paths:
                        if import_path in line:
                            line = line.replace(import_path, ''.join([f'{package_name}.', import_path]), 1)
                            break
                elif line.startswith('import'):
                    parts = line.split()
                    if parts[1] in base_pys:
                        line = line.replace('import', f'from {package_name} import')
                
                new_lines.append(line)

        with open(filename, 'w') as file:
            file.write(''.join(new_lines))
