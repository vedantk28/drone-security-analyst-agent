# 🛡️ Drone Security Analyst Agent

A modular AI-powered surveillance system that analyzes drone frame captions and telemetry data to detect suspicious activity, generate alerts, and support semantic search .

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/vedantk28/drone-security-analyst-agent.git
cd drone-security-analyst-agent
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Manual Investigation Workflow
```bash
python -m src.langchain_agent  
```

---

## 🧠 Design Decisions & Architecture

### 🔧 Modular Toolchain
* **QueryDetectionsTool** – Searches object detections by keyword
* **AlertCheckTool** – Applies rule-based logic to flag suspicious events
* **RetrieverTool** – Semantic search over detection logs using FAISS
* **FrameRetrieverTool** – Semantic search over BLIP-generated captions

### 🧱 Architecture Overview
```
[frame_captions.json] + [telemetry.json]
           ↓
     FrameEvent objects
           ↓
     ┌───────────────┐
     │ alert_engine  │ → alerts.json
     └───────────────┘
           ↓
     ┌───────────────┐
     │ vector_store  │ → FAISS indexes
     └───────────────┘
           ↓
     ┌────────────────────────────┐
     │ langchain_tools   │
     └────────────────────────────┘
```

### 🤖 AI Tools Integrated
| Tool | Purpose | Impact |
|------|---------|--------|
| **BLIP** | Captioning frames | Enables semantic search and visual reasoning |
| **FAISS** | Vector indexing | Fast retrieval of similar events and captions |
| **LangChain Tools** | Modular orchestration | Clean execution of detection and retrieval |



---

## 🧪 Testing Documentation

### ✅ Unit Tests
* `test_alert_engine.py` – Validates alert rules: loitering, crowd, truck
* `test_input_generator.py` – Verifies location inference and telemetry format
*  `test_langchain_tools.py` – Can check tool invocations

### 🧪 Dynamic Scenarios
* **Midnight Loitering** – Person spotted at Gate at 00:03
* **Crowd in Urban Zone** – Caption triggers alert based on zone
* **Truck Cluster** – Detected in Truck Yard during operation
* **Non-alert Case** – Dog at Garage at 14:15 passes without alert

---

## 📂 Data Artifacts

* `frame_captions.json` – BLIP-generated image captions
* `telemetry.json` – Timestamp, location, and altitude data
* `alerts.json` – Triggered alerts
* `vector_index/` & `frame_index/` – FAISS indexes for search

---


---

## 🚀 Features

- **Automated Alert Generation**: Rule-based detection of suspicious activities
- **Semantic Search**: Find relevant events using natural language queries
- **Modular Design**: Easy to extend with new detection rules and tools
- **Comprehensive Testing**: Unit tests and dynamic scenario validation

---

## 📋 Requirements

- Python 3.8+
- Virtual environment support
- Dependencies listed in `requirements.txt`

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

