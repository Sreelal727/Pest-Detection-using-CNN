Here is a sample README file for your project:

---

# Pest Detection using CNN

This project leverages a **Convolutional Neural Network (CNN)** to detect pests in real-time using live video feed from an ESP32-CAM and classify them into different categories. The model is trained on pest images and predicts the class when given new image inputs. This system helps in early pest detection, aiding in preventing potential crop damage.

---

## Project Structure

- **Training Code**: The training script (`train.py`) preprocesses images, builds a CNN model, and trains it on a dataset of pest images. The model is saved for future use in real-time testing.
- **Testing Code**: The testing script (`test.py`) uses the trained model to analyze live video feed from an ESP32-CAM, predicting the pest class. Based on the predicted pest class, the system performs actions via an ESP32 microcontroller to control actuators.
- **Dataset**: Pest images are stored in the `data` folder, with each subfolder containing images of a specific pest class.

## Prerequisites

- Python 3.6 or later
- Required Python libraries:
  - `opencv-python`
  - `tensorflow`
  - `skimage`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `pandas`
  - `scikit-learn`
  - `requests`
  - `Pillow`
  - `tkinter`
  - `serial`

You can install the required libraries using:

```bash
pip install -r requirements.txt
```

## Data Preprocessing

The training data must be organized into separate folders for each pest class within a `data` directory.

```
data/
    ├── Class1/
    ├── Class2/
    └── Class3/
```

The images are preprocessed by:
- Resizing them to 100x100 pixels.
- Applying normalization.
- Splitting the dataset into training and test sets.

## Model Architecture

The CNN architecture used in this project consists of:
- Three convolutional layers followed by max-pooling.
- Two fully connected (dense) layers.
- A final softmax layer with 15 output neurons corresponding to the number of pest classes.

The model uses `sparse_categorical_crossentropy` as the loss function and `adam` optimizer.

## Training the Model

To train the model, run the training script:

```bash
python train.py
```

The model will be trained for 15 epochs, and the performance will be tracked. Training and validation accuracy and loss graphs will be displayed upon completion. The model will be saved as `CNN.model`.

## Live Pest Detection

The testing code involves capturing live video from the ESP32-CAM and running real-time pest detection using the trained CNN model. Based on the prediction, actions are triggered via the ESP32 microcontroller.

To run the real-time pest detection, execute:

```bash
python test.py
```

- Press **'q'** to perform a frame analysis.
- The pest class will be displayed on the Tkinter GUI.
- The system interacts with an ESP32 microcontroller for triggering control actions (e.g., activating an actuator for pest control) based on the detected pest.

## Confusion Matrix and Classification Report

At the end of testing, a confusion matrix and classification report will be generated to evaluate the model's performance on the test data.

## ESP32-CAM and Serial Communication

The system communicates with the ESP32-CAM for video feed capture and uses serial communication with the ESP32 microcontroller to trigger actions based on pest detection.

## Model Performance

Once the training and testing are completed, the accuracy, loss, and confusion matrix will be displayed to evaluate the model's performance.

## Future Improvements

- Increase the dataset size for better generalization.
- Implement more advanced techniques like transfer learning for enhanced accuracy.
- Extend the system to detect more pest classes.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to modify or expand upon this README as per your project's specific requirements!
