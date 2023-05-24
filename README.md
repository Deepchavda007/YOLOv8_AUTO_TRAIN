# YOLO_AUTO_TRAIN - Automated Training for YOLOv8 Object Detection Model

## Description
YOLO_AUTO_TRAIN is a Python script that enables automated training for the YOLOv8 object detection model. It simplifies the process of creating YAML files, setting up the training environment, and training the model.

## Prerequisites
- [Ultralytics library](https://pypi.org/project/ultralytics/) (Please make sure it is installed)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/YOLO_AUTO_TRAIN.git


## Dataset Format

```yaml
dataset/
  train/
    images/
      image1.jpg
      image2.jpg
      ...
    labels/
      image1.txt
      image2.txt
      ...
  test/
    images/
      image3.jpg
      image4.jpg
      ...
    labels/
      image3.txt
      image4.txt
      ...
  test/
    image3.jpg
    image4.jpg

```
## Parameters
* **user_name:** The username or owner of the project.
* **val_dataset_path:** Path to the validation dataset.
* **train_dataset_path:** Path to the training dataset.
* **class_names:** List of class names.
* **num_class:** Number of classes.
* **model_name:** Name of the YOLOv8 model to use.
* **pretrained:** Whether to use a pretrained model.
* **project_name:** Name of the project.
* **experiment_name:** Name of the experiment.
* **save_model_name:** Name of the saved model file.
* **num_epochs:** Number of training epochs.
* **imgsz:** Image size for training.
* **batch_size:** Batch size for training.
* **device:** Device to use for training.(0 for gpu use)


## Output
* The script will train the YOLOv8 model and save the best performing model to the specified **`save_model_name`** file. The file path of the saved model will be returned by the training method.
