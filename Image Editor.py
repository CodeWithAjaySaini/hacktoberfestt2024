from PIL import Image, ImageEnhance
import os

def open_image(file_path):
    """Open an image file."""
    try:
        img = Image.open(file_path)
        print(f"Image {file_path} opened successfully.")
        return img
    except Exception as e:
        print(f"Error opening image: {e}")
        return None

def save_image(img, save_path):
    """Save the edited image."""
    try:
        img.save(save_path)
        print(f"Image saved as {save_path}.")
    except Exception as e:
        print(f"Error saving image: {e}")

def resize_image(img, new_size):
    """Resize the image to new dimensions."""
    return img.resize(new_size)

def rotate_image(img, angle):
    """Rotate the image by a given angle."""
    return img.rotate(angle)

def change_brightness(img, factor):
    """Change the brightness of the image."""
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

def main():
    print("Simple Image Editor")
    file_path = input("Enter the path to the image file: ")
    
    # Open the image
    img = open_image(file_path)
    if img is None:
        return

    while True:
        print("\nOptions:")
        print("1. Resize Image")
        print("2. Rotate Image")
        print("3. Change Brightness")
        print("4. Save Image")
        print("5. Quit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            img = resize_image(img, (width, height))
            print(f"Image resized to {width}x{height}.")
        
        elif choice == '2':
            angle = int(input("Enter rotation angle (degrees): "))
            img = rotate_image(img, angle)
            print(f"Image rotated by {angle} degrees.")

        elif choice == '3':
            factor = float(input("Enter brightness factor (0.0 to 1.0): "))
            img = change_brightness(img, factor)
            print(f"Brightness changed by a factor of {factor}.")

        elif choice == '4':
            save_path = input("Enter the path to save the edited image: ")
            save_image(img, save_path)

        elif choice == '5':
            print("Exiting the image editor. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
