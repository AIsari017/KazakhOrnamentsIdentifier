from PIL import Image
import os
import random

base_images_folder = ""  # folder containing the ornament images
overlay_images_folder = ""  # folder containing the overlay images
output_folder = ""  # folder for the final images

overlay_images = []
for filename in os.listdir(overlay_images_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):  
        overlay_image = Image.open(os.path.join(overlay_images_folder, filename))
        overlay_images.append(overlay_image)

# list all base images
base_images = [f for f in os.listdir(base_images_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

os.makedirs(output_folder, exist_ok=True)

# process each base image
for idx, base_image_name in enumerate(base_images):
    # load the base image
    base_image_path = os.path.join(base_images_folder, base_image_name)
    base_image = Image.open(base_image_path)

    # get the corresponding overlay image in round-robin fashion
    overlay_image = overlay_images[idx % len(overlay_images)]

    # ensure the base image fits within the overlay image by resizing if needed
    base_image = base_image.resize((overlay_image.width, overlay_image.height))

    # generate random position for pasting (make sure the base image doesn't exceed overlay bounds)
    max_x = overlay_image.width - base_image.width
    max_y = overlay_image.height - base_image.height
    random_x = random.randint(0, max_x)
    random_y = random.randint(0, max_y)

    # paste the base image on top of the overlay image at the random position
    overlay_image.paste(base_image, (random_x, random_y), base_image)

    # save the result
    output_image_path = os.path.join(output_folder, f"result_{base_image_name}")
    overlay_image.save(output_image_path)

print("All images processed successfully!")
