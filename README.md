# Virtual Painter

Virtual Painter is an interactive application that allows users to draw on a virtual canvas using hand gestures captured through a webcam. The project utilizes computer vision techniques to track hand movements, detect gestures, and enable users to draw with different colors.

## Development Environment

This project was developed using the following tools:

- IDE: Visual Studio Code

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Run the `virtual_painter.py` script.

## Packages:
 - OpenCV 
 - MediaPipe
 - Numpy
NB: All these packages need to be installed properly.

## Usage

- Upon running the application, your webcam will be activated, and you'll see a window displaying the virtual canvas.
- Use your hand gestures to interact with the canvas. Raise two fingers to select colors and draw, and use specific finger gestures to switch between drawing and selection modes.
- Experiment with different hand movements to draw shapes, lines, or any creative artwork you desire.

## Hand Landmark
![Hand Landmarks](images/HandCoordinates.jpg)

## Conclusion:
The Virtual Painter project demonstrates the feasibility of creating a hands-free drawing application using computer vision techniques. By enabling users to draw and interact with a virtual canvas through hand gestures, the project opens up new possibilities for creative expression and interactive experiences. Further enhancements could include additional drawing tools, improved gesture recognition, and compatibility with different devices, expanding the project's functionality and usability.

## Result:
![Virtual Painter Video](images/gifvideo.gif)
