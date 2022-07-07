import os
import glob
import shutil
import random           #  shutil.copy(src=dirpath+'/'+i, dst=r'Dr_Drowsiness_Detection\MRL Eye Data\Prepared_Data\Close Eyes')

from tqdm import tqdm

raw_data = r'C:\Users\Boyko\Desktop\ps\ps\mrlEyes_2018_01'
for dirpath, dirname, filename in os.walk(raw_data):
    for file in tqdm([f for f in filename if f.endswith('.png')]):
        if file.split('_')[4] == '0':
            path=r'C:\Users\Boyko\Desktop\ps\ps\data\train\closed'
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy(src=dirpath + '/' + file, dst= path)
        elif file.split('_')[4] == '1':
            path= r'C:\Users\Boyko\Desktop\ps\ps\data\train\open'
            if not os.path.exists(path):
                os.makedirs(path)
            shutil.copy(src=dirpath + '/' + file, dst= path)  
           
def create_test_closed(source, destination, percent):
   
    path, dirs, files_closed = next(os.walk(source))
    file_count_closed = len(files_closed)
    percentage = file_count_closed * percent
    to_move = random.sample(glob.glob(source + "/*.png"), int(percentage))

    for f in enumerate(to_move):
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.move(f[1], destination)
    print(f'moved {int(percentage)} images to the destination successfully.')    
    
def create_test_open(source, destination, percent):
    
    path, dirs, files_open = next(os.walk(source))
    file_count_open = len(files_open)
    percentage = file_count_open * percent
    to_move = random.sample(glob.glob(source + "/*.png"), int(percentage))

    for f in enumerate(to_move):
        if not os.path.exists(destination):
            os.makedirs(destination)
        shutil.move(f[1], destination)
    print(f'moved {int(percentage)} images to the destination successfully.')
    
create_test_closed(r'C:\Users\Boyko\Desktop\ps\ps\data\train\closed', 
                    r'C:\Users\Boyko\Desktop\ps\ps\data\test\closed', 
                    0.2)
create_test_open(r'C:\Users\Boyko\Desktop\ps\ps\data\train\open', 
                    r'C:\Users\Boyko\Desktop\ps\ps\data\test\open', 
                    0.2)