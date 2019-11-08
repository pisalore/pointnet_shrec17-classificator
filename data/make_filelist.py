import os
import glob

FILES = './pts_dir'

if not os.path.exists('./filelist.txt'):
    print('Writing filelist...\n')
    f = open('filelist.txt', 'a')
    print(glob.glob(os.path.join(FILES, '*.pts')))

    for path_file in glob.glob(os.path.join(FILES, '*.pts')):
        file = os.path.basename(path_file)
        print(file)
        file_name = str(file.split('.')[0])
        print(file_name)
        f.write(file_name + '\n')
    print('Filelist created.')
else:
    print('filelist.txt already exists.')