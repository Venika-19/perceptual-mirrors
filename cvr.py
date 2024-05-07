import cv2

def overlay_image(background_image_path, foreground_image_path, output_path):
    # Read the background and foreground images
    background = cv2.imread(background_image_path)
    foreground = cv2.imread(foreground_image_path)

    # Resize the foreground image to match the size of the background image
    foreground = cv2.resize(foreground, (background.shape[1], background.shape[0]))

    # Blend the foreground image onto the background image
    blended = cv2.addWeighted(background, 1, foreground, 1, 0)

    # Save the result
    cv2.imwrite(output_path, blended)

# Example usage:
background_image_path = "1.jpg"
foreground_image_path = "norm_up.jpg"
output_path = "output_image_with_overlay.jpg"

overlay_image(background_image_path, foreground_image_path, output_path)
