# Linear Algebraic Ray Tracer

A custom-built ray tracing engine written from scratch using Python, NumPy, and PyGame. This project focuses on visual realism, lighting behavior, reflections, and camera movement with a linear algebraic approach rather than the standard geometrical fashion.

**Full formatted technical paper:**  
[raytracer.pdf](./raytracer.pdf)

---

## Visual Highlights

### Scene With Increasing Depth

![Depth Scene](assets/depth_scene.png)

---

### Specular Highlights (Blinn–Phong)

![Specular Highlights](assets/specular.png)

---

### Recursive Reflections

![Reflections](assets/reflection.png)

---

### Live Camera View (PyGame)

![Live View](assets/live_view.png)

---

### Wireframe Projection Overlay

![Wireframe](assets/wireframe.png)

---

## What This Project Does

- Ray traced rendering
- Diffuse + specular lighting
- Recursive reflections
- Real camera system with yaw/pitch + movement
- Live interactive render viewport
- Wireframe cube
- Static high-quality image renders

Everything is built on:
- Vector math
- Matrix transformations
- Coordinate space conversions

---

## Controls (Live Mode)

- W / S → forward / backward  
- A / D → strafe left / right  
- Space / Shift → up / down  
- Mouse → camera rotation  

Current performance: ~0.5 FPS  
Planned optimization via Numba or lower-level implementation.