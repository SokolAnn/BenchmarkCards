# EMMOE (Embodied Mobile Manipulation in Open Environments)

## 📊 Benchmark Details

**Name**: EMMOE (Embodied Mobile Manipulation in Open Environments)

**Overview**: EMMOE is a benchmark aimed at evaluating autonomous home robots' capabilities to interpret user instructions and execute long-horizon everyday tasks in continuous space. It integrates high-level and low-level embodied tasks into a unified framework, featuring new evaluation metrics and the EMMOE-100 dataset with various task attributes.

**Data Type**: task sequences with detailed annotations

**Domains**:
- Robotics
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ALFRED
- OVMM

**Resources**:
- [GitHub Repository](https://github.com/OpenDriveLab/EMMOE)
- [Resource](https://huggingface.co/datasets/EMMOE)
- [Resource](https://www.youtube.com/@EMMOE-Project)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and advance the development of intelligent autonomous robots through the execution of language-based tasks.

**Target Audience**:
- ML Researchers
- Robotics Developers
- Industry Practitioners

**Tasks**:
- Mobile Manipulation
- Task Planning

**Limitations**: N/A

## 💾 Data

**Source**: EMMOE-100 dataset collected using the Fetch robot in Habitat-Lab 2.0.

**Size**: 100 tasks with 966 subtasks

**Format**: JSON, images of execution

**Annotation**: Manually annotated with task attributes, execution success status, and feedback mechanisms after failures.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Task Progress (TP)
- Success Rate (SR)
- Success End Rate (SER)
- Success Re-plan Rate (SRR)

**Calculation**: Metrics are calculated based on task execution success, keypath sequences for TP, and counting re-plans for SRR.

**Interpretation**: Higher values in TP, SR, SER, and SRR indicate better performance and reliability of the robotic agent.

**Baseline Results**: HOMIE BOT-7B with SFT+DPO achieved high success rates across various metrics.

**Validation**: Benchmark validated through systematic comparison of performance across multiple robotic models and tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack, Data poisoning
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data is derived from legally compliant sources and attributed to original creators.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
