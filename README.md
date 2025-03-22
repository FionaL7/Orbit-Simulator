# 🪐 Orbit Simulator

An interactive 3D orbit simulator built using **VPython** to visualize planetary motion based on Kepler's laws of planetary motion. This project simulates how planets revolve around a star with realistic orbital mechanics.

## Features

- Simulates planetary orbits with elliptical paths.
- Real-time visualization of orbital motion.
- Adjustable orbital parameters like semi-major axis and eccentricity.
- Calculates and displays perihelion and aphelion distances.
- Supports planetary systems with moons.
- Dynamic trails and orbital paths.

## Technologies Used

- **Python**
- **VPython** for 3D visualization
- **NumPy** for mathematical calculations

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/orbit-simulator.git
   cd orbit-simulator
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the simulator:
   ```bash
   python app.py
   ```

## How It Works

- The simulator uses Kepler's laws and Newtonian mechanics to calculate planetary positions.
- The equation for the distance of the planet from the star is given by:

  \[ r = \frac{a(1 - e^2)}{1 + e \cdot \cos(\theta)} \]

  Where:

  - \( a \) = Semi-major axis
  - \( e \) = Eccentricity
  - \( \theta \) = True anomaly (angle of the planet from perihelion)

- The gravitational force and angular velocity are calculated using Newton's law of gravitation.

## Usage

- Adjust parameters like semi-major axis and eccentricity directly in the code for different simulations.
- Watch how the planet accelerates near the perihelion and slows down near the aphelion.
- View dynamic trails that map out the orbit over time.

## Acknowledgments

- Built using **VPython** for realistic 3D visualizations.
- Inspired by the beauty of celestial mechanics and astrophysics.
