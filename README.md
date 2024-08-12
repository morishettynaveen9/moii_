# Object Detection with YOLOv5

## Overview

This project uses YOLOv5 for object detection on images. It detects objects in images, draws bounding boxes, counts objects, and saves results to a JSON file.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Place your images in the `images/` folder.
2. Run the script:
   ```bash
   python script.py
   ```
3. The output will be saved in the `output_images/` folder and `results.json`.

## Examples

- **Detect objects and plot bounding boxes:**

  ```bash
  python script.py
  ```

- **Query object count via API (if implemented):**
  ```bash
  curl http://localhost:8000/query?frame_name=car.jpg
  ```

## Contributing

If you'd like to contribute, please fork the repository and submit a pull request with your changes.

## Sample Images

The `images/` folder contains sample images for testing. You can replace these with your own images, but ensure they are in formats supported by the script (e.g., `.jpg`, `.png`).

Sample images include:

- `car.jpg` - An image of a car.
- `person.jpg` - An image of a person.
- `dog.jpg` - An image of a dog.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
