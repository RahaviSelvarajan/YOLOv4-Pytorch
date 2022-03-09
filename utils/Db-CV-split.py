import os
import glob
import shutil

root_dir = '/content/onedrive/Dataset/'

def train_test_split(root_dir, test_fold):
    dest_folder = '/content/darknet/data'
    for i, folder in enumerate(os.listdir(root_dir)):
      folder_path = os.path.join(root_dir, folder)
      file_list = [image for image in glob.glob(os.path.join(folder_path, '*.jpg'))]
      if i != test_fold:
        with open('train.txt' , 'w') as file:
          for image in file_list:
              file.write(image)
              file.write("\n")
          file.close()
      else:
        with open('test.txt' , 'w') as file:
          for image in file_list:
              file.write(image)
              file.write("\n")
          file.close()
    shutil.copy('train.txt', dest_folder)
    shutil.copy('test.txt', dest_folder)