# Linear Algebraic Ray Tracer

A custom-built ray tracing engine written from scratch using Python, NumPy, and PyGame. This project focuses on visual realism, lighting behavior, reflections, and camera movement, all created by a linear algebra–driven rendering pipeline.

**Full formatted technical paper:**  
[raytracer.pdf](./raytracer.pdf)

---

## Visual Highlights

### Scene With Increasing Depth
Demonstrates correct perspective scaling and object depth ordering.

![Depth Scene](assets/depth_scene.png)

---

### Specular Highlights (Blinn–Phong)
Shows glossy surface response under a defined light source.

![Specular Highlights](assets/specular.png)

---

### Recursive Reflections
Reflective surfaces recursively bounce light and color.

![Reflections](assets/reflection.png)

---

### Live Camera View (PyGame)
Real-time camera traversal using WASD and mouse look.

![Live View](assets/live_view.png)

---

### Wireframe Projection Overlay
Real-time projected cube rendered over the ray-traced scene for verification.

![Wireframe](assets/wireframe.png)

---

## What This Project Does

- Renders spheres using ray tracing  
- Supports **diffuse + specular lighting**
- Supports **recursive reflections**
- Uses a **real camera system** with yaw/pitch + movement
- Displays a **live interactive render viewport**
- Overlays a **wireframe cube using matrix projection**
- Generates static high-quality renders as image files

Everything is built on top of:
- Vector math
- Matrix transformations
- Coordinate space conversions

---

## Controls (Live Mode)

- **W / S** → forward / backward  
- **A / D** → strafe left / right  
- **Space / Shift** → up / down  
- **Mouse** → camera rotation  

Current performance: ~0.5 FPS  
Planned optimization via Numba or lower-level implementation.