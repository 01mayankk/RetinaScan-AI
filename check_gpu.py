import torch

print("PyTorch Version:", torch.__version__)

print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():

    print("GPU Name:", torch.cuda.get_device_name(0))

    print("GPU Count:", torch.cuda.device_count())

    print("Current Device:", torch.cuda.current_device())

else:
    print("No GPU detected")