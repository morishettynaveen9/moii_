import os
import json
import cv2
import numpy as np
import torch
from typing import List, Dict
from flask import Flask, jsonify

app = Flask(__name__)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load YOLOv5 small model

def read_images_from_folder(folder_path: str) -> List[str]:
    """Reads image file paths from a given folder."""
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

def detect_objects(image_path: str) -> List[Dict[str, float]]:
    """Detects objects in an image using YOLOv5 and returns bounding boxes."""
    img = cv2.imread(image_path)
    results = model(img)
    boxes = []
    for *box, conf, cls in results.xyxy[0]:
        x1, y1, x2, y2 = map(int, box)
        boxes.append({'x': x1, 'y': y1, 'w': x2 - x1, 'h': y2 - y1})
    return boxes

def plot_bounding_boxes(image_path: str, boxes: List[Dict[str, float]]) -> np.ndarray:
    """Draws bounding boxes on an image and returns the image with boxes."""
    image = cv2.imread(image_path)
    for box in boxes:
        x, y, w, h = box['x'], box['y'], box['w'], box['h']
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return image

def count_objects(boxes: List[Dict[str, float]]) -> int:
    """Counts the number of bounding boxes (objects) in an image."""
    return len(boxes)

def save_results(results: Dict[str, int], output_path: str) -> None:
    """Saves the results to a JSON file."""
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=4)

@app.route('/query_objects/<frame_name>', methods=['GET'])
def query_objects(frame_name: str) -> Dict[str, int]:
    """API endpoint to query the number of objects in a given frame."""
    if frame_name in object_counts:
        return jsonify({frame_name: object_counts[frame_name]})
    else:
        return jsonify({'error': 'Frame not found'}), 404

if __name__ == '__main__':
    image_folder = './images'
    output_json = './object_counts.json'

    images = read_images_from_folder(image_folder)
    results = {}

    for image_path in images:
        base_name = os.path.basename(image_path)
        frame_name = os.path.splitext(base_name)[0]
        boxes = detect_objects(image_path)
        image_with_boxes = plot_bounding_boxes(image_path, boxes)
        num_objects = count_objects(boxes)
        results[frame_name] = num_objects
        cv2.imwrite(f'./output/{base_name}', image_with_boxes)

    save_results(results, output_json)
    object_counts = results

    app.run(host='0.0.0.0', port=5000)
