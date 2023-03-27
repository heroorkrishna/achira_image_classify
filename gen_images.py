import os
import argparse
import random
from PIL import Image, ImageDraw, ImageOps


# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate images with random shapes')
parser.add_argument('input_folder', type=str, help='Path to folder containing input shapes')
parser.add_argument('output_folder', type=str, help='Path to folder to output generated images')
parser.add_argument('--out-dims', nargs=2, type=int, default=[1024, 1024], help='Dimensions of output image')
parser.add_argument('--num-images', type=int, default=1000, help='Number of images to generate')
args = parser.parse_args()


# Load input shapes
input_shapes = []
for filename in os.listdir(args.input_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        input_shapes.append(Image.open(os.path.join(args.input_folder, filename)).convert('RGBA'))


# Set up output image and draw object
output_dims = tuple(args.out_dims)
output_image = Image.new('RGBA', output_dims, (255, 255, 255, 0))
draw = ImageDraw.Draw(output_image)


# Determine number of each shape to add to output image
num_shapes = len(input_shapes)
shapes_per_image = [int(args.num_images // num_shapes) for _ in range(num_shapes)]
remainder = args.num_images % num_shapes
for i in range(remainder):
    shapes_per_image[i] += 1


# Determine dimensions of each shape in output image
shape_dims = []
for shape in input_shapes:
    shape_dims.append((int(shape.width * 0.75), int(shape.height * 0.75)))


# Generate output images
for i in range(args.num_images):
    # Determine position and size of each shape
    shapes = []
    for j, shape in enumerate(input_shapes):
        for k in range(shapes_per_image[j]):
            shape_pos = (random.randint(0, output_dims[0] - shape_dims[j][0]), random.randint(0, output_dims[1] - shape_dims[j][1]))
            shape_size = (random.randint(shape_dims[j][0], output_dims[0] - shape_pos[0]), random.randint(shape_dims[j][1], output_dims[1] - shape_pos[1]))
            shapes.append((shape.crop((0, 0, shape.width, shape.height)).resize(shape_size, Image.ANTIALIAS), shape_pos))

    # Add shapes to output image
    random.shuffle(shapes)
    for shape, pos in shapes:
        angle = random.randint(0, 90)
        shape = shape.rotate(angle, expand=True)
        output_image.alpha_composite(shape, dest=pos)

    # Save output image
    filename = f'image_{i+1}.png'
    output_image.save(os.path.join(args.output_folder, filename))

    # Clear output image
    output_image = Image.new('RGBA', output_dims, (255, 255, 255, 0))