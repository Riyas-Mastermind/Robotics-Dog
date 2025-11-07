# 🤖 Robotics-Dog

### Developed using **PilotX Microcontroller**  
*By Safear Defense Private Limited – Bengaluru*  

---

## 📘 Overview

The **Robotics-Dog** project demonstrates an intelligent quadruped robot designed to mimic animal-like movements using **MicroPython** on the **PilotX microcontroller**.  
This project is part of the *learning-based robotics and embedded control* initiative and aims to help students and developers understand the fundamentals of **multi-servo motion control**, **pose transitions**, and **autonomous behavior**.

---

## ⚙️ PilotX Microcontroller — Overview

The **PilotX Microcontroller**, developed by **Safear Defense Private Limited – Bengaluru**, is a high-performance embedded control platform engineered for robotics, UAVs, and autonomous systems.  
It supports **MicroPython programming**, **real-time telemetry**, and **sensor-rich applications**, making it ideal for projects like the **Robotics-Dog**.

### 🔧 Technical Specifications
- 🧩 **12 Configurable I/O Pins** (Digital / PWM / Analog)  
- 📡 **Built-In 2.4GHz Telemetry & Receiver**  
- 📶 **PPM Input Compatibility** for RC integration  
- 🧭 **Built-In Compass (Magnetometer)**  
- 🌐 **GPS Module Support via UART**  
- 🔌 **I²C Bus Support for 16+ Sensors**  
- ⚡ **Operating Voltage:** 3.3V – 5.0V  

### 🧠 Programming & Development
- **Language:** MicroPython  
- **Connection:** USB / 2.4GHz Wireless  
- **Firmware:** Upgradable via bootloader  
- **Applications:** Robotics, IoT, Drones, Research  

---

## 💻 PlannerX Ground Control Station

**PlannerX**, developed by *Safear Defense Private Limited – Bengaluru*, is a comprehensive **Ground Control Station (GCS)** software used for real-time monitoring, parameter tuning, and mission planning.  
It supports a wide range of vehicles — including **rovers**, **robotic arms**, **rockets**, and **drones** — and integrates seamlessly with the **PilotX** platform.

### 🚀 Features
- Real-time telemetry monitoring  
- PID tuning and parameter configuration  
- Mission and path planning tools  
- Graphical dashboards for system visualization  
- Multiple vehicle profiles (Rover, Drone, Robot Arm, Rocket)  
- **100% Offline Operation — Free Lifetime Access**

### 📥 Download & Access
- **Software:** PlannerX GCS  
- **Developer:** Safear Defense Pvt. Ltd. – Bengaluru  
- **Platform:** Windows  
- **License:** Free (Lifetime Access)  
- **Documentation:** [Read Manual](#) *(Insert your manual or PDF link here)*  

---

## 🐾 Robotics Dog — Project Explanation

### 🎯 Project Goals
- Design a **quadruped robot** that performs realistic, smooth movements.  
- Implement **pose-based servo control** using MicroPython.  
- Demonstrate interactive actions such as **handshake**, **walking**, and **sleeping**.  
- Integrate motion logic, sensors, and control software.

---

### ⚙️ System Logic Overview

The robot dog is driven by **eight servo motors**, each controlling a leg joint.  
The project uses **MicroPython** to coordinate servo movement through **smooth interpolation** and **pose sequencing**.

#### 🧩 Key Components:
1. **Servo Initialization:**  
   Sets all 8 servos to a neutral (standing) position.

2. **Smooth Motion Function:**  
   A custom routine (`move_servos_smooth()`) incrementally adjusts servo angles to reach target positions.  
   This ensures **smooth and lifelike movements** instead of abrupt transitions.

3. **Defined Poses:**
   - 🐕 **Stand Pose:** Default upright position  
   - 🪑 **Sit Pose:** Lowers hind legs to simulate sitting  
   - 💤 **Sleep Pose:** Full rest mode  
   - ⚙️ **Work Pose:** Active operational stance  

4. **Action Sequences:**
   - **Handshake Motion:** The robot raises and lowers its front leg repeatedly.  
   - **Pose Transitions:** Moves sequentially through stand → sit → sleep → work positions.  
   - **Walking Sequence:** Alternates leg positions for a natural walking cycle (20 seconds).  

5. **Timing Control:**  
   Uses `utime` and `sleep()` for accurate delay management and motion pacing.

---

### 🧠 Learning Outcomes
By completing this project, you will learn to:
- Control multiple servos in synchronization using MicroPython  
- Develop **pose-based motion sequences**  
- Implement **smooth servo interpolation** for natural movement  
- Design simple robotic behaviors and routines  

---

### 🛠️ Hardware Setup
| Component | Description |
|------------|-------------|
| Microcontroller | PilotX (Safear Defense Pvt. Ltd.) |
| Servo Motors | 8 × 180° Standard Servos |
| Power Supply | 5V DC (2A or above recommended) |
| Communication | 2.4GHz Telemetry (PlannerX) |
| Optional | GPS, Compass, Ultrasonic, IMU |

---

### 🧩 Software Setup
- **Programming Language:** MicroPython  
- **IDE / Tool:** PlannerX or any MicroPython IDE  
- **Upload Method:** USB / Telemetry Interface  
- **Execution:** Continuous motion loop sequence  

---

### 🧱 Future Enhancements
- Integration of **IMU sensors** for dynamic balance  
- **Voice or gesture-based control** features  
- **Autonomous path navigation** using ultrasonic & GPS modules  
- Real-time **pose visualization** in PlannerX  

---

### 🏢 About Safear Defense Pvt. Ltd.
**Safear Defense Private Limited**, based in **Bengaluru, India**, is a technology-driven company specializing in **robotics, autonomous systems, and defense-grade embedded solutions**.  
Their innovations such as **PilotX** and **PlannerX** enable developers, researchers, and students to explore cutting-edge embedded intelligence and robotics technologies.

---

### 📄 License
This project is open for **educational and non-commercial use** under standard open-source guidelines.  
Please credit *Safear Defense Pvt. Ltd.* when using or modifying this work.

---

**© 2025 Safear Defense Private Limited – Bengaluru**  
*Innovating Intelligence in Robotics and Embedded Systems*
