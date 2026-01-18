import imageio
from scipy import ndimage
import matplotlib.pyplot as plt
from skimage import transform, filters, color


# --------------------------------------------------
# STEP 1: Load the image from file
# --------------------------------------------------
# Reads the image as a NumPy array (H x W x 3 for RGB)
original_image = imageio.imread('image_of_parrot.jpg')

# Display the original image
plt.imshow(original_image)
plt.title("Original Image")
plt.axis("off")
plt.show()


# --------------------------------------------------
# STEP 2: Rotate the image
# --------------------------------------------------
# Rotate the image by 45 degrees
# ndimage.rotate automatically handles resizing
rotated_image = ndimage.rotate(original_image, 45)

# Display rotated image
plt.imshow(rotated_image)
plt.title("Rotated Image (45°)")
plt.axis("off")
plt.show()


# --------------------------------------------------
# STEP 3: Apply Gaussian blur
# --------------------------------------------------
# sigma controls the amount of blur (higher = more blur)
blurred_image = ndimage.gaussian_filter(rotated_image, sigma=3)

# Display blurred image
plt.imshow(blurred_image)
plt.title("Blurred Image (Gaussian Filter)")
plt.axis("off")
plt.show()


# --------------------------------------------------
# STEP 4: Resize the image
# --------------------------------------------------
# Resize image to (height=600, width=100)
# transform.resize returns a floating-point image
resized_image = transform.resize(original_image, (600, 100))

# Compare original and resized images
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original Image')
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(resized_image)
plt.title('Rescaled Image')
plt.axis("off")

plt.show()


# --------------------------------------------------
# STEP 5: Convert image to grayscale
# --------------------------------------------------
# rgb2gray converts RGB image to 2D grayscale image
grayscale_image = color.rgb2gray(original_image)


# --------------------------------------------------
# STEP 6: Edge detection using Sobel filter
# --------------------------------------------------
# Sobel filter highlights edges in the image
edges = filters.sobel(grayscale_image)

# Display original image and edge-detected image
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original Color Image')
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='viridis')
plt.title('Edge-Detected Image')
plt.axis("off")

plt.show()
