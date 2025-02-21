from PIL import Image
import random
import os

ornament_dir = "" # folder containing the ornament images
background_dir = "" # folder containing the overlay images
output_folder = "" # folder for the final images

ornament_paths = [os.path.join(ornament_dir, f) for f in os.listdir(ornament_dir) if f.endswith(('.png', '.jpg'))]
background_paths = [os.path.join(background_dir, f) for f in os.listdir(background_dir) if f.endswith(('.png', '.jpg'))]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

random.shuffle(background_paths)

# counter for naming the output files
counter = 1

for _ in range(120): 
    bg_path = random.choice(background_paths)
    background = Image.open(bg_path).convert("RGBA")

    ornament_path = random.choice(ornament_paths)
    ornament = Image.open(ornament_path)

    # resize ornament if larger than the background while maintaining aspect ratio
    if ornament.width > background.width or ornament.height > background.height:
        ornament.thumbnail((background.width, background.height), Image.Resampling.LANCZOS)

    #randomly resize the ornament between 50% and 150% of its current size
    size_factor = random.uniform(0.5, 1.5)
    ornament = ornament.resize((int(ornament.width * size_factor), int(ornament.height * size_factor)),
                               Image.Resampling.LANCZOS)

    # randomly rotate the ornament
    ornament = ornament.rotate(random.randint(0, 360), expand=True)

    # ensure the ornament is still smaller than the background after resizing and rotating
    if ornament.width > background.width or ornament.height > background.height:
        ornament.thumbnail((background.width, background.height), Image.Resampling.LANCZOS)

    # randomly select a position to paste the ornament
    max_x = background.width - ornament.width
    max_y = background.height - ornament.height
    paste_position = (random.randint(0, max_x), random.randint(0, max_y))

    # paste the ornament onto the background using alpha blending (RGBA)
    ornament = ornament.convert("RGBA")
    background.paste(ornament, paste_position, ornament)  

    # save the new image with the new naming convention
    ornament_basename = os.path.splitext(os.path.basename(ornament_path))[0]
    new_image_path = os.path.join(output_folder, f"{ornament_basename}_{counter}.png")
    background.save(new_image_path, format="PNG")
    counter += 1

print(f"Generated {counter-1} images.")