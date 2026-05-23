import os
import random
import shutil

from PIL import Image
from torchvision import transforms

# =====================================
# PATHS
# =====================================
input_base = "../../dataset/classified_images"

output_base = "../../dataset/balanced_dataset"

TARGET_COUNT = 300

# =====================================
# AUGMENTATION
# =====================================
augment = transforms.Compose([

    transforms.RandomHorizontalFlip(),

    transforms.RandomRotation(20),

    transforms.ColorJitter(
        brightness=0.2,
        contrast=0.2
    ),
])

# =====================================
# CREATE OUTPUT FOLDERS
# =====================================
for i in range(5):

    os.makedirs(
        os.path.join(output_base, str(i)),
        exist_ok=True
    )

# =====================================
# PROCESS EACH CLASS
# =====================================
for class_name in os.listdir(input_base):

    class_path = os.path.join(
        input_base,
        class_name
    )

    if not os.path.isdir(class_path):
        continue

    images = [

        img for img in os.listdir(class_path)

        if img.endswith(
            ('.png', '.jpg', '.jpeg')
        )
    ]

    print(f"\n📂 Processing Class {class_name}")
    print(f"Original Count: {len(images)}")

    output_class_path = os.path.join(
        output_base,
        class_name
    )

    # =================================
    # CASE 1 → UNDERSAMPLING
    # =================================
    if len(images) >= TARGET_COUNT:

        selected = random.sample(
            images,
            TARGET_COUNT
        )

        for img_name in selected:

            src = os.path.join(
                class_path,
                img_name
            )

            dst = os.path.join(
                output_class_path,
                img_name
            )

            shutil.copy(src, dst)

    # =================================
    # CASE 2 → AUGMENTATION
    # =================================
    else:

        # Copy original images
        for img_name in images:

            src = os.path.join(
                class_path,
                img_name
            )

            dst = os.path.join(
                output_class_path,
                img_name
            )

            shutil.copy(src, dst)

        current_count = len(images)

        while current_count < TARGET_COUNT:

            img_name = random.choice(images)

            img_path = os.path.join(
                class_path,
                img_name
            )

            image = Image.open(
                img_path
            ).convert("RGB")

            augmented = augment(image)

            new_name = (
                f"aug_{current_count}_{img_name}"
            )

            augmented.save(

                os.path.join(
                    output_class_path,
                    new_name
                )
            )

            current_count += 1

    final_count = len(
        os.listdir(output_class_path)
    )

    print(f"✅ Final Count: {final_count}")

# =====================================
# COMPLETE
# =====================================
print("\n🎉 Dataset Balancing Completed!")