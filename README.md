# 🤖 Robotics-Dog  
### Developed using **PilotX Microcontroller**  
**By Safear Defense Private Limited – Bengaluru**  
**3-Day Workshop conducted at BMS College of Engineering**

---

## 📘 Overview

The **Robotics-Dog** project showcases an intelligent quadruped robot designed to mimic animal-like movements using **MicroPython** on the **PilotX microcontroller**.  
This project was developed and demonstrated during a **3-day hands-on workshop at BMS College of Engineering**, aimed at teaching students real-world applications of **robotics, embedded systems, and motion control**.

The workshop focused on **learning-based robotics development**, helping students and developers understand the fundamentals of **multi-servo motion control**, **pose transitions**, and **autonomous behavior** through practical experimentation.

---

## ⚙️ PilotX Microcontroller — Overview

The **PilotX Microcontroller**, developed by **Safear Defense Private Limited – Bengaluru**, is a high-performance embedded control platform engineered for **robotics, UAVs, and autonomous systems**.  
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
- **Firmware:** Upgradable via Bootloader  
- **Applications:** Robotics, IoT, Drones, Research  

---

## 💻 PlannerX Ground Control Station

**PlannerX**, developed by *Safear Defense Private Limited – Bengaluru*, is a comprehensive **Ground Control Station (GCS)** software used for **real-time monitoring, parameter tuning, and mission planning**.  
It supports a wide range of vehicle types — including **rovers, robotic arms, rockets, and drones** — and integrates seamlessly with the **PilotX** platform.

### 🚀 Features
- Real-time telemetry monitoring  
- PID tuning and parameter configuration  
- Mission and path planning tools  
- Graphical dashboards for visualization  
- Multi-vehicle support (Rover, Drone, Robotic Arm, Rocket)  
- **100% Offline Operation — Free Lifetime Access**

### 📥 Download & Access
- **Software:** PlannerX GCS  
- **Developer:** Safear Defense Pvt. Ltd. – Bengaluru  
- **Platform:** Windows  
- **License:** Free (Lifetime Access)  
- **Documentation:** [Read Manual](#)

---

## 🐾 Robotics Dog — Project Explanation

### 🎯 Project Goals
- Design a **quadruped robot** that performs realistic, smooth movements.  
- Implement **pose-based servo control** using MicroPython.  
- Demonstrate interactive actions such as **handshake**, **walking**, and **sleeping**.  
- Integrate motion logic, sensors, and software for smart behavior.

---

### ⚙️ System Logic Overview

The robot dog is driven by **eight servo motors**, each controlling a leg joint.  
The system uses **MicroPython** to coordinate servo movement through **smooth interpolation** and **pose sequencing**.

#### 🧩 Key Components
1. **Servo Initialization:**  
   Sets all servos to a neutral (standing) position.

2. **Smooth Motion Function (`move_servos_smooth()`):**  
   Moves servos gradually to their target angles for lifelike motion.

3. **Defined Poses:**
   - 🐕 **Stand Pose:** Upright neutral stance  
   - 🪑 **Sit Pose:** Rear legs lowered  
   - 💤 **Sleep Pose:** Fully relaxed position  
   - ⚙️ **Work Pose:** Active mode  

4. **Action Sequences:**
   - 🤝 **Handshake Motion:** Raises and lowers front leg repeatedly.  
   - 🔁 **Pose Transitions:** Moves through stand → sit → sleep → work positions.  
   - 🚶 **Walking Sequence:** Alternates leg movements to simulate walking (20 seconds).  

5. **Timing Control:**  
   Uses `utime` and `sleep()` for precise motion pacing.

---

### 🧠 Learning Outcomes
By completing this workshop project, participants learned how to:
- Control multiple servos using **MicroPython**  
- Create **pose-based robotic movement sequences**  
- Implement **smooth servo interpolation** for realistic motion  
- Design simple robotic behaviors with embedded logic  

---

### 🛠️ Hardware Setup
| Component | Description |
|------------|-------------|
| **Microcontroller** | PilotX (Safear Defense Pvt. Ltd.) |
| **Servo Motors** | 8 × 180° Standard Servos |
| **Power Supply** | 5V DC (2A or above) |
| **Communication** | 2.4GHz Telemetry via PlannerX |
| **Optional Modules** | GPS, Compass, Ultrasonic, IMU |

---

### 🧩 Software Setup
- **Programming Language:** MicroPython  
- **IDE / Tool:** PlannerX or compatible MicroPython IDE  
- **Upload Method:** USB / Telemetry Interface  
- **Execution:** Continuous motion control sequence  

---

### 🧱 Future Enhancements
- Integration of **IMU sensors** for dynamic balance  
- **Voice or gesture control** support  
- **Autonomous walking** with GPS and ultrasonic sensors  
- Real-time **pose visualization** in PlannerX  

---

## 🏫 Workshop Context — BMS College of Engineering

This project was part of a **3-Day Hands-On Robotics & Embedded Systems Workshop** conducted at **BMS College of Engineering**, in collaboration with **Safear Defense Private Limited – Bengaluru**.  
Participants learned about:
- Embedded control with the **PilotX microcontroller**  
- Programming in **MicroPython**  
- Robotic motion design and servo interfacing  
- Real-time control using **PlannerX GCS**

The workshop concluded with a live demonstration of the **Robotics-Dog** performing handshake, walking, and pose sequences.

---

## 🏢 About Safear Defense Pvt. Ltd.

**Safear Defense Private Limited**, based in **Bengaluru, India**, specializes in **robotics, autonomous systems, and defense-grade embedded technologies**.  
Their innovations — **PilotX** (microcontroller platform) and **PlannerX** (GCS software) — enable students, engineers, and researchers to build intelligent, real-time robotic systems.

---

## 📄 License
This project is open for **educational and non-commercial use** under standard open-source guidelines.  
Please credit *Safear Defense Pvt. Ltd.* when using or adapting this work.

---

**© 2025 Safear Defense Private Limited – Bengaluru**  
*Innovating Intelligence in Robotics and Embedded Systems*
