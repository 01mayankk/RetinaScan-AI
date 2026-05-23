import os
import random
import shutil

# =====================================
# PATHS
# =====================================
source_dir = "../../dataset/balanced_dataset"

train_dir = "../../dataset/train"
val_dir = "../../dataset/val"
test_dir = "../../dataset/test"

# =====================================
# SPLIT RATIOS
# =====================================
train_ratio = 0.70
val_ratio = 0.15
test_ratio = 0.15

# =====================================
# CREATE CLASS FOLDERS
# =====================================
for base_dir in [train_dir, val_dir, test_dir]:

    for i in range(5):

        os.makedirs(
            os.path.join(base_dir, str(i)),
            exist_ok=True
        )

# =====================================
# PROCESS EACH CLASS
# =====================================
for class_name in os.listdir(source_dir):

    class_path = os.path.join(
        source_dir,
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

    random.shuffle(images)

    total = len(images)

    train_count = int(total * train_ratio)

    val_count = int(total * val_ratio)

    # =================================
    # SPLIT
    # =================================
    train_images = images[:train_count]

    val_images = images[
        train_count:
        train_count + val_count
    ]

    test_images = images[
        train_count + val_count:
    ]

    # =================================
    # COPY TRAIN
    # =================================
    for img in train_images:

        shutil.copy(

            os.path.join(class_path, img),

            os.path.join(
                train_dir,
                class_name,
                img
            )
        )

    # =================================
    # COPY VAL
    # =================================
    for img in val_images:

        shutil.copy(

            os.path.join(class_path, img),

            os.path.join(
                val_dir,
                class_name,
                img
            )
        )

    # =================================
    # COPY TEST
    # =================================
    for img in test_images:

        shutil.copy(

            os.path.join(class_path, img),

            os.path.join(
                test_dir,
                class_name,
                img
            )
        )

    # =================================
    # OUTPUT
    # =================================
    print(f"\n📂 Class {class_name}")

    print(f"Train: {len(train_images)}")

    print(f"Validation: {len(val_images)}")

    print(f"Test: {len(test_images)}")

# =====================================
# COMPLETE
# =====================================
print("\n🎉 Dataset Split Completed!")
