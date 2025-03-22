import os
from vpython import sphere, vector, rate, scene, ring, label, curve
from math import cos, sin, sqrt, pi

# Scene setup
scene.range = 6  # Dark navy background
scene.background = vector(0.1, 0.1, 0.2)
scene.width = 1400
scene.height = 600
scene.center = vector(0, 0, 0)
scene.fullscreen = True
scene.userzoom = False

# Constants
G = 1
M = 1
a = 4
e = 0.5
dt = 0.01
r = a
angle = 0
v = sqrt(G * M * (1 + e) / r)

# Star and planetary setup
star = sphere(pos=vector(0, 0, 0), radius=1,
              color=vector(1, 1, 0), emissive=True)
star_label = label(pos=star.pos, text='Central Star\n(Gravitational Center)',
                   xoffset=40, yoffset=40, box=False, opacity=0.7)


planet = sphere(
    pos=vector(a, 0, 0),
    radius=0.3,
    color=vector(0.3, 0.6, 1),
    make_trail=True,
    retain=100
)
label1 = label(pos=planet.pos, text='Planet 1', xoffset=20,
               yoffset=20, box=False, opacity=0.5)
label1.pos = planet.pos
label1.text = f"r: {r:.2f}, v: {v:.2f}"
planet.trail_color = vector(0, 1, 0)

trail_r = abs(cos(angle))
trail_g = abs(sin(angle))
planet.trail_color = vector(trail_r, trail_g, 0.5)


# PLANET 2
a2 = 4.5
e2 = 0.3
r2 = a2
v2 = sqrt(G * M * (1 + e2) / r2)
angle2 = 0

planet2 = sphere(
    pos=vector(1.5 * a, 0, 0),
    radius=0.2,
    color=vector(1, 0.5, 0.3),
    make_trail=True,
    retain=100
)


# MOON
moon_orbit_radius = 0.5
moon_speed = 2.5
moon = sphere(pos=planet.pos + vector(moon_orbit_radius, 0, 0), radius=0.2,
              color=vector(0.6, 0.6, 0.6), make_trail=True,
              trail_type="curve",
              retain=100)
moon_angle = 0
moon_distance = 0.2
moon_velocity = sqrt(G * M / moon_distance)


# Energy labels
kinetic_label = label(pos=vector(3, -0.3, 0), text='Kinetic Energy: ',
                      box=False, height=12, color=vector(0, 1, 0))
potential_label = label(pos=vector(
    3, -0.5, 0), text='Potential Energy: ', box=False, height=12, color=vector(1, 0, 0))

info_box = label(
    pos=scene.center + vector(0, -3, 0),
    text='Kinetic Energy: 0\nPotential Energy: 0',
    box=True,
    border=10,
    color=vector(1, 1, 1),
    background=vector(0.2, 0.2, 0.2)
)

# Simulation loop
while True:
    rate(100)
    # PLANET 1
    angle += (v / r) * dt
    r = (a * (1 - e**2)) / (1 + e * cos(angle))
    v = sqrt(G * M * (1 + e) / r)
    planet.pos = vector(r * cos(angle), r * sin(angle), 0)

    # PLANET 2
    angle2 += (v2 / r2) * dt
    r2 = (a2 * (1 - e2**2)) / (1 + e2 * cos(angle2))
    v2 = sqrt(G * M * (1 + e2) / r2)
    planet2.pos = vector(r2 * cos(angle2), r2 * sin(angle2), 0)

    # MOON
    moon_angle += moon_speed * dt
    moon.pos = planet.pos + vector(moon_orbit_radius * cos(moon_angle),
                                   moon_orbit_radius * sin(moon_angle), 0)

    kinetic_energy = 0.5 * (v**2)
    potential_energy = -G * M / r
    kinetic_label.text = f"Kinetic Energy: {kinetic_energy:.2f}"
    potential_label.text = f"Potential Energy: {potential_energy:.2f}"
    info_box.text = f"Kinetic Energy: {
        kinetic_energy:.2f}\nPotential Energy: {potential_energy:.2f}"
