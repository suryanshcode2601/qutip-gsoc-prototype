# README.md

````markdown
# Interactive Bloch Sphere Prototype

This prototype was developed by **Suryansh Chandel**, a prospective participant for **Google Summer of Code 2026** from **Motilal Nehru National Institute of Technology (MNNIT), Allahabad, India**.

The goal of this project is to explore interactive visualization of qubit states using a Bloch sphere.
As an initial step, I developed a working prototype that allows users to visualize and interact with basic quantum states on the Bloch sphere using QuTiP and Matplotlib.
This prototype serves as a starting point for further development of more advanced interactive features.

---

## Features

The current prototype includes:

- Interactive **Bloch sphere visualization**
- Buttons to switch between common qubit states:
  - |0⟩
  - |1⟩
  - |+⟩
  - |−⟩
- Real-time update of the Bloch vector when states are changed
- Sliders to control the viewing angles:
  - **Azimuth**
  - **Elevation**
- Single-window interface using Matplotlib widgets

---

## Technologies Used

- Python
- QuTiP (Quantum Toolbox in Python)
- Matplotlib

---

## Installation

Install the required dependencies:

```bash
pip install qutip matplotlib 
````

---

## Running the Prototype

Run the script using:

```bash
python test_bloch.py
```

This will open an interactive window displaying the Bloch sphere with controls.

---

## Development Notes

During development, several issues were encountered and resolved:

* Initial environment configuration issues while installing QuTiP
* Module import errors due to incorrect Python environment paths
* Bloch sphere and UI controls appearing in separate figures

The final implementation resolves these by explicitly binding the Bloch object to the Matplotlib figure and axes, allowing the entire interface to be rendered within a single window.

---

## Future Improvements

Potential improvements for future versions include:

* Adding quantum gate operations (X, Y, Z)
* Animating qubit state rotations
* Allowing arbitrary state input
* Supporting multi-qubit visualization
* Improving the UI layout and interaction design

---

## Screenshot

An example output of the prototype is included in this repository.

---

## Author

**Suryansh Chandel**  
suryanshwork3456@gmail.com
Prospective GSoC 2026 Participant  
Motilal Nehru National Institute of Technology (MNNIT), Allahabad  
India
