import cv2

def overlay_image(background_image_path, foreground_image_path, output_path):
    background = cv2.imread(background_image_path)
    foreground = cv2.imread(foreground_image_path)
    foreground = cv2.resize(foreground, (background.shape[1], background.shape[0]))
    blended = cv2.addWeighted(background, 1, foreground, 1, 0)
    cv2.imwrite(output_path, blended)

background_image_path = "norm_up.jpg"
foreground_image_path = "1.jpg"
output_path = "3.jpg"

overlay_image(background_image_path, foreground_image_path, output_path)
