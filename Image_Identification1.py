import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Define the file path and the width
filename = '/content/runs/detect/train/confusion_matrix.png'
width = 600

# Load and display the image
img = mpimg.imread(filename)
height = img.shape[0] * width / img.shape[1]

plt.figure(figsize=(width / 100, height / 100))
plt.imshow(img)
plt.axis('off')  # Hide the axes
plt.show()
