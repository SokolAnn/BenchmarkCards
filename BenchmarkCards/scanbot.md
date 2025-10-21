# ScanBot

## 📊 Benchmark Details

**Name**: ScanBot

**Overview**: ScanBot is the first instruction-conditioned, multimodal dataset designed explicitly for high-precision surface scanning tasks in robotic systems. It targets the shortcomings of existing datasets by providing synchronized multimodal observations, including RGB, depth, and laser profiles, paired with natural language instructions for a variety of scanning tasks.

**Data Type**: multimodal

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- RoboTurk
- MIME
- RoboNet
- BridgeData
- BC-Z
- RT-1
- MT-Opt
- RoboSet
- RH20T
- DROID
- Open X-Embodiment

**Resources**:
- [GitHub Repository](https://github.com/username/ScanBot)

## 🎯 Purpose and Intended Users

**Goal**: To develop a dataset that enables research on tool-specific embodied perception beyond traditional manipulation, facilitating instruction-conditioned policy learning in robotic surface scanning.

**Target Audience**:
- ML Researchers
- Roboticists
- Industry Practitioners

**Tasks**:
- Surface Scanning
- Defect Inspection
- Comparative Analysis
- Functional Target Scanning

**Limitations**: The current version of ScanBot assumes flat surfaces, limiting its applicability to objects with curved or irregular geometries. It is also designed for open-loop scanning which does not adapt based on scan quality during execution.

## 💾 Data

**Source**: Dataset generated through a structured protocol involving high-precision sensors and a robotic system.

**Size**: 896 scans

**Format**: multimodal data including RGB, depth, and laser profiles

**Annotation**: Data annotated with multi-task natural language commands.

## 🔬 Methodology

**Methods**:
- Model evaluation through benchmarking VLA models on specific scanning tasks.

**Metrics**:
- Surface Reconstruction Accuracy
- Waypoint Jitter Minimization
- Instruction Grounding Accuracy

**Calculation**: Model performance metrics are calculated based on the accuracy of selected scanner parameters, localization of objects based on instructions, and fidelity of the reconstructed surfaces compared to ground-truth.

**Interpretation**: Higher accuracy metrics indicate better model performance in generating stable scanning trajectories and precise interpretations of natural language instructions.

**Baseline Results**: Existing VLA models show poor performance with average accuracies below 50% in selection of parameters and task execution.

**Validation**: Validation procedures involve comparing model outputs against ground-truth scans captured under controlled conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: ['Misalignment in scanning leading to poor data quality.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
