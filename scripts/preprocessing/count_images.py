import os

# =====================================
# DATASET PATH
# =====================================
base_folder = "../../dataset/classified_images"

print("\n📊 Classified Dataset Count\n")

total = 0

# =====================================
# COUNT IMAGES
# =====================================
for folder in sorted(os.listdir(base_folder)):

    folder_path = os.path.join(
        base_folder,
        folder
    )

    if os.path.isdir(folder_path):

        count = len([
            file for file in os.listdir(folder_path)
            if file.endswith(('.png', '.jpg', '.jpeg'))
        ])

        total += count

        print(f"Class {folder}: {count} images")

# =====================================
# TOTAL
# =====================================
print(f"\nTotal Images: {total}")