import torch
import torch.nn as nn

class StandardCNN(nn.Module):
    """
    Standard Canonical 2-Stage CNN Architecture
    Stage 1: Conv -> ReLU -> Pool -> Conv -> ReLU -> Pool
    Stage 2: Flatten -> Linear -> ReLU -> Dropout -> Linear
    """
    def __init__(self, in_channels=1, num_classes=10):
        super(StandardCNN, self).__init__()

        # Stage 1: Feature Extraction
        self.features = nn.Sequential(
            # Block 1
            nn.Conv2d(in_channels=in_channels, out_channels=32, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2),

            # Block 2
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )

        # Stage 2: Dense Classification Head
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(in_features=64 * 5 * 5, out_features=64),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(in_features=64, out_features=num_classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x

if __name__ == "__main__":
    print("=" * 60)
    print("PYTORCH CNN ARCHITECTURE VERIFICATION & PARAMETER BREAKDOWN")
    print("=" * 60)

    model = StandardCNN(in_channels=1, num_classes=10)
    print(model)

    dummy_input = torch.randn(4, 1, 28, 28)
    output = model(dummy_input)
    print(f"\nDummy Input Batch Shape : {dummy_input.shape}")
    print(f"Output Predictions Shape: {output.shape}")

    total_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"\nTotal Trainable Parameters: {total_params:,}")

    print("\nLayer-by-Layer Parameters:")
    for name, param in model.named_parameters():
        print(f"  {name:30s} : {str(param.shape):20s} ({param.numel():,} params)")
