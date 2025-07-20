# 🛡️ Drone Security Analyst Agent

A modular AI-powered surveillance system that analyzes drone frame captions and telemetry data to detect suspicious activity, generate alerts, and support semantic search .

## ✅ Requirements Coverage

### 1. Feature Specification

**Value to Property Owners:** Enhances perimeter security through automated surveillance and intelligent event analysis. The agent autonomously monitors drone video feeds, identifies unusual patterns (e.g., crowd formation after midnight), triggers alerts, and supports natural language investigations — reducing dependency on manual monitoring and improving response time.

**Key Requirements Addressed:**
- **Automated monitoring via frame captioning and telemetry inference**
- **Real-time alert generation based on rule-based anomaly detection**
- **Conversational querying of surveillance data using an agent pipeline**

### 2. Design / Architecture

**Proposed Architecture:**
- **Frame Ingestion:** Frames simulated via BLIP captioning
- **Telemetry Module:** Infers location and timestamp from captions
- **Alert Engine:** Applies security rules (e.g., object-location-time combinations)
- **Indexer:** Stores structured `FrameEvent` objects with semantic metadata
- **Semantic Retriever:** Searches indexed events using FAISS
- **Agent Orchestration:** LangChain tools + DialoGPT for reasoning and response

Architecture was validated using AI-guided modular development and visualized using a Mermaid diagram (see `/docs/system_architecture.md`).

### 3. Development

- **Language:** Python
- **Simulation:** Used `generate_sample_data()` to create synthetic frames like:
  - `"Frame 109: a large crowd gathered near a gate under low light"`
  - `"Time: 00:03, Location: Urban Zone"`
- **AI-Generated Components:**
  - Captioning via **BLIP** (HuggingFace model)
  - Prompt engineering + tool chaining via **LangChain**
  - Rule-based alert engine scaffolding co-designed using **Copilot**

All components were modularized under `/src`, tested using simulated data, and orchestrated via `main.py`.

### 4. Cross-Domain Indexing

- **Indexing System:** Implemented a frame-by-frame semantic index using FAISS. Each `FrameEvent` contains object, location, timestamp, and caption text.
- **Storage Format:** Events are stored in structured JSON (`data/indexed_frames.json`) for traceability and semantic retrieval.
- **AI Guidance:** Used Copilot to design the indexing pipeline and embedding strategy.

### 5. QA and Validation

- **Unit Tests:** Test cases created under `/tests` to verify:
  - Truck events correctly indexed
  - Midnight crowd alerts are triggered
  - Agent returns coherent responses based on FAISS search
- **Integration Testing:** `main.py` simulates full pipeline: data generation → alert triggers → indexing → agent response.
- **Manual QA via Semantic Queries:** Sample agent query: `"Were any buses near the Garage?"` Response: `"Yes, detections of a bus near the Garage triggered alerts around 14:00."`

AI tools (Copilot + LangChain + DialoGPT) assisted in generating test flows, debugging logic, and validating conversational outputs.

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

### 4. Run the Investigation Workflow
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


## 📦 Dataset Support

### Current Implementation
- **Synthetic Data**: Generated via BLIP captioning with simulated telemetry
- **Flexible Architecture**: Designed for easy integration with real-world datasets

### VisDrone Dataset (Reference)
The system is architected to seamlessly integrate with **VisDrone** - a large-scale benchmark for visual analysis from UAV platforms:

- **Maintained by**: Tsinghua University & Huawei
- **Coverage**: Diverse urban scenes across China
- **Content**: Video sequences and annotated images with bounding boxes, object categories, and occlusion indicators
- **Categories**: Pedestrians, vehicles, bicycles, buses, trucks, and crowd scenes
- **Applications**: Tracking, detection, and dense surveillance analytics

### 🔍 Relevance to Production
- Real-world captions and detections from VisDrone can replace synthetic inputs
- Object types (bus, crowd, person) align with existing alert rules
- Benchmark semantic retrieval and evaluate emergency responses under high-density scenarios



### Setup Instructions

#### 1️⃣ Generate Telemetry from Captions
```bash
python -m src.input_generator
```
Populates `telemetry.json` with inferred timestamps and locations.

#### 2️⃣ Trigger Alert Engine
```bash
python -m src.alert_engine
```
Processes frame events and generates `alerts.json`.

#### 3️⃣ Create Semantic Indexes (FAISS)
```bash
python -m src.vector_store
```
Builds and saves FAISS indexes in `vector_index/` and `frame_index/`.

#### 4️⃣ Run Manual Investigation Workflow
```bash
python -m src.langchain_agent
```
Performs detection queries, semantic search, alert scanning, and frame retrieval using LangChain tools and DialoGPT agent.

#### 5️⃣ Run Test Suite (Optional)
```bash
python tests/test_alert_engine.py
python tests/test_input_generator.py
python tests/test_langchain_agent.py
```
Validates alert logic, telemetry generation, and tool invocations.

## 🏗️ Architecture

### Core Components

- **Input Generator** (`src.input_generator`): Processes raw surveillance data and generates structured telemetry
- **Alert Engine** (`src.alert_engine`): Real-time alert detection based on predefined rules and patterns
- **Vector Store** (`src.vector_store`): FAISS-based semantic indexing for efficient frame retrieval
- **LangChain Agent** (`src.langchain_agent`): AI-powered investigation workflow with natural language querying

### Data Flow

1. **Raw Data Input** → Surveillance frames with BLIP captions
2. **Telemetry Generation** → Structured metadata with timestamps and locations
3. **Alert Processing** → Real-time detection of security events
4. **Semantic Indexing** → Vector embeddings for similarity search
5. **Investigation Interface** → AI-powered query and analysis tools

## 📁 Project Structure

```
├── src/
│   ├── input_generator.py      # Telemetry generation
│   ├── alert_engine.py         # Alert detection logic
│   ├── vector_store.py         # FAISS indexing
│   └── langchain_agent.py      # AI investigation workflow
├── tests/                      # Test suite
├── vector_index/               # FAISS indexes (generated)
├── frame_index/                # Frame embeddings (generated)
├── telemetry.json             # Generated telemetry data
├── alerts.json                # Generated alerts
└── requirements.txt           # Dependencies
```

## 🔧 Configuration

### Alert Rules
Alert detection can be customized in `src/alert_engine.py` for different object categories:
- Pedestrian detection in restricted areas
- Vehicle anomaly detection
- Crowd density monitoring
- Emergency situation identification

### Vector Store Settings
Semantic search parameters can be adjusted in `src/vector_store.py`:
- Embedding model selection
- FAISS index configuration
- Similarity thresholds

## 🧪 Testing

The system includes comprehensive tests for all major components:

```bash
# Run all tests
python -m pytest tests/

# Run specific test files
python tests/test_alert_engine.py
python tests/test_input_generator.py
python tests/test_langchain_agent.py
```

## 🔮 Future Enhancements

- **Real-time Streaming**: Integration with live UAV feeds
- **Advanced ML Models**: Custom object detection and tracking models
- **Web Interface**: Dashboard for real-time monitoring and investigation
- **Multi-UAV Coordination**: Support for multiple surveillance sources
- **Enhanced Analytics**: Behavioral pattern recognition and predictive alerts



---


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

