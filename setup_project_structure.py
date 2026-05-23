import os

# ==========================================
# PROJECT ROOT
# ==========================================
ROOT = "."

# ==========================================
# COMPLETE PROJECT STRUCTURE
# ==========================================
folders = [

    # ======================================
    # DATASET
    # ======================================
    "dataset",

    "dataset/raw_images",
    "dataset/classified_images",
    "dataset/balanced_dataset",

    "dataset/train",
    "dataset/val",
    "dataset/test",

    # Train class folders
    "dataset/train/0",
    "dataset/train/1",
    "dataset/train/2",
    "dataset/train/3",
    "dataset/train/4",

    # Validation class folders
    "dataset/val/0",
    "dataset/val/1",
    "dataset/val/2",
    "dataset/val/3",
    "dataset/val/4",

    # Test class folders
    "dataset/test/0",
    "dataset/test/1",
    "dataset/test/2",
    "dataset/test/3",
    "dataset/test/4",

    # ======================================
    # SCRIPTS
    # ======================================
    "scripts",

    # PREPROCESSING
    "scripts/preprocessing",

    # TRAINING
    "scripts/training",

    # UTILS
    "scripts/utils",

    # ======================================
    # MODELS
    # ======================================
    "models",
    "models/checkpoints",
    "models/saved_models",

    # ======================================
    # OUTPUTS
    # ======================================
    "outputs",

    "outputs/predictions",
    "outputs/heatmaps",
    "outputs/metrics",
    "outputs/confusion_matrix",
    "outputs/logs",

    # ======================================
    # NOTEBOOKS
    # ======================================
    "notebooks",

    # ======================================
    # APPLICATION
    # ======================================
    "app",
]

# ==========================================
# CREATE FOLDERS
# ==========================================
print("\n🚀 Creating Project Structure...\n")

for folder in folders:

    path = os.path.join(ROOT, folder)

    os.makedirs(path, exist_ok=True)

    print(f"✅ Created: {folder}")

# ==========================================
# IMPORTANT FILES
# ==========================================
files = [

    # ROOT FILES
    "requirements.txt",
    "README.md",
    ".gitignore",

    # ======================================
    # PREPROCESSING FILES
    # ======================================
    "scripts/preprocessing/classify_images.py",
    "scripts/preprocessing/balance_dataset.py",
    "scripts/preprocessing/split_dataset.py",
    "scripts/preprocessing/count_images.py",
    "scripts/preprocessing/count_balanced_dataset.py",

    # ======================================
    # TRAINING FILES
    # ======================================
    "scripts/training/train_model.py",
    "scripts/training/evaluate_model.py",
    "scripts/training/test_model.py",
    "scripts/training/inference.py",
    "scripts/training/metrics.py",

    # ======================================
    # UTILITY FILES
    # ======================================
    "scripts/utils/dataset_utils.py",
    "scripts/utils/image_utils.py",
    "scripts/utils/config.py",

    # ======================================
    # APP FILES
    # ======================================
    "app/main.py",
    "app/gradcam.py",
    "app/app_utils.py",
]

# ==========================================
# CREATE FILES
# ==========================================
print("\n📄 Creating Important Files...\n")

for file in files:

    if not os.path.exists(file):

        with open(file, "w") as f:
            pass

        print(f"✅ Created: {file}")

    else:
        print(f"⚠️ Already Exists: {file}")

# ==========================================
# SUCCESS MESSAGE
# ==========================================
print("\n🎉 COMPLETE PROFESSIONAL PROJECT STRUCTURE CREATED!")
print("\n📁 Your RetaniaScan-AI project is now fully organized.")