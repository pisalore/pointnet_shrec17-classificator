import os
import glob

FILES = '.\pts_dir'
LABEL_DIR = '.\label_dir'

filenames_training = [line.rstrip() for line in open("filelist_training.txt", 'r')]
filenames_testing = [line.rstrip() for line in open("filelist_testing.txt", 'r')]

if not os.path.exists(LABEL_DIR):
     os.mkdir(LABEL_DIR)
print('Generating labels...')
for path_file in glob.glob(os.path.join(FILES, '*.pts')):
    file = os.path.basename(path_file)
    file_name = file.split('.')[0]
    label_file_path = os.path.join(LABEL_DIR, file_name + '.seg')
    f = open(label_file_path, 'a')

for path_file in glob.glob(os.path.join(LABEL_DIR, '*.seg')):
    class_file = path_file.split('\\')[2].split('_')[0]
    f = open(path_file, 'w+')
    if (class_file == 'class1'):
            f.write('0' + '\n')
    elif (class_file == 'class2'):
            f.write('1' + '\n')
    elif (class_file == 'class3'):
            f.write('2' + '\n')
    elif (class_file == 'class4'):
            f.write('3' + '\n')
    elif (class_file == 'class5'):
            f.write('4' + '\n')
    elif (class_file == 'class6'):
            f.write('5' + '\n')
    elif (class_file == 'class7'):
            f.write('6' + '\n')
    elif (class_file == 'class8'):
            f.write('7' + '\n')
    elif (class_file == 'class9'):
            f.write('8' + '\n')
    elif (class_file == 'class10'):
            f.write('9' + '\n')
    elif (class_file == 'class11'):
            f.write('10' + '\n')
    elif (class_file == 'class12'):
            f.write('11' + '\n')
    elif (class_file == 'class13'):
            f.write('12' + '\n')
    elif (class_file == 'class14'):
            f.write('13' + '\n')
    elif (class_file == 'class15'):
            f.write('14' + '\n')
print('Label files generated.')

