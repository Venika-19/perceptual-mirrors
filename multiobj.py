import cv2
import numpy as np
import os



def combine_images(folder1_images, folder2_images, folder3_images):
    combined_images = []
    for img1, img2, img3 in zip(folder1_images, folder2_images, folder3_images):
        max_height = max(img1.shape[0], img2.shape[0], img3.shape[0])
        total_width = img1.shape[1] + img2.shape[1] + img3.shape[1]
        background = np.ones((max_height, total_width, 3), dtype=np.uint8) * 255

        background[0:img1.shape[0], 0:img1.shape[1]] = img1
        background[0:img2.shape[0], img1.shape[1]:img1.shape[1] + img2.shape[1]] = img2
        background[0:img3.shape[0], img1.shape[1] + img2.shape[1]:] = img3
        
        combined_images.append(background)
    return combined_images

images_cats = []
for filename in os.listdir('cats_2'):
  img = cv2.imread(os.path.join('cats_2', filename))
  images_cats.append(img)
images_dogs = []
for filename in os.listdir('dogs_2'):
  img = cv2.imread(os.path.join('dogs_2', filename))
  images_dogs.append(img)
images_pandas = []
for filename in os.listdir('panda_2'):
  img = cv2.imread(os.path.join('panda_2', filename))
  images_pandas.append(img)


combined_images = combine_images(images_dogs, images_cats, images_pandas)


output_folder = 'combined_images'
os.makedirs(output_folder, exist_ok=True)

for i, img in enumerate(combined_images):
    cv2.imwrite(os.path.join(output_folder, f'combined_image_{i}.jpg'), img)


