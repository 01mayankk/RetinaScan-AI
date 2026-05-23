import pandas as pd
import os
import shutil

# =====================================
# PATHS
# =====================================
csv_file = "../../dataset/train.csv"

image_folder = "../../dataset/raw_images"

output_folder = "../../dataset/classified_images"

# =====================================
# READ CSV
# =====================================
df = pd.read_csv(csv_file)

# =====================================
# CREATE CLASS FOLDERS
# =====================================
for i in range(5):

    os.makedirs(
        os.path.join(output_folder, str(i)),
        exist_ok=True
    )

# =====================================
# CLASSIFY IMAGES
# =====================================
count = 0
missing = 0

for _, row in df.iterrows():

    image_name = row['id_code'] + ".png"

    source_path = os.path.join(
        image_folder,
        image_name
    )

    diagnosis = str(row['diagnosis'])

    destination_path = os.path.join(
        output_folder,
        diagnosis,
        image_name
    )

    if os.path.exists(source_path):

        shutil.copy(source_path, destination_path)

        count += 1

        print(f"✅ Copied: {image_name}")

    else:

        missing += 1

        print(f"❌ Missing: {image_name}")

# =====================================
# FINAL OUTPUT
# =====================================
print("\n🎉 Classification Completed!")
print(f"Copied Images : {count}")
print(f"Missing Images: {missing}")