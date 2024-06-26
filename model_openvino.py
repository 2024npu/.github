import torch
import torch.onnx
import torchvision.models as models

# Load your pre-trained PyTorch model
model = models.resnet18(pretrained=True)
model.eval()

# Dummy input for the model
dummy_input = torch.randn(1, 3, 224, 224)

# Export the model to ONNX format
torch.onnx.export(model, dummy_input, "model.onnx", 
                  input_names=["input"], output_names=["output"], 
                  opset_version=11)

from openvino.inference_engine import IECore
import numpy as np
import cv2

# Initialize OpenVINO runtime
ie = IECore()

# Read the IR model
model_xml = "model_ir/model.xml"
model_bin = "model_ir/model.bin"
net = ie.read_network(model=model_xml, weights=model_bin)

# Load the model to the CPU (or specify other device like GPU)
exec_net = ie.load_network(network=net, device_name="CPU")

# Prepare an input image
image = cv2.imread("input_image.jpg")
image = cv2.resize(image, (224, 224))
image = image.transpose(2, 0, 1)  # Change data layout from HWC to CHW
image = image.reshape(1, 3, 224, 224)  # Add batch dimension
image = image.astype(np.float32)

# Perform inference
input_blob = next(iter(net.input_info))
output_blob = next(iter(net.outputs))
result = exec_net.infer({input_blob: image})

# Process the output
output = result[output_blob]
print("Inference result:", output)