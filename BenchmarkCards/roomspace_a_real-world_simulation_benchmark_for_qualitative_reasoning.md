# RoomSpace (A Real-World Simulation Benchmark for Qualitative Reasoning)

## 📊 Benchmark Details

**Name**: RoomSpace (A Real-World Simulation Benchmark for Qualitative Reasoning)

**Overview**: This paper presents a novel benchmark for assessing qualitative spatial reasoning (QSR) in language models, grounded in realistic 3D simulation data, offering a series of diverse room layouts with various objects and their spatial relationships.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- bAbI
- StepGame
- SpartQA
- SpaRTUN

**Resources**:
- [Resource](https://doi.org/10.5518/1518)
- [GitHub Repository](https://github.com/Fangjun-Li/RoomSpace)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language models' capabilities in qualitative spatial reasoning using realistic scenarios derived from 3D simulations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Qualitative Spatial Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: 3D simulation data utilizing the ProcTHOR framework.

**Size**: 10,000 rooms

**Format**: Textual narratives with associated spatial relationship data.

**Annotation**: Automated generation based on spatial relationship constraints.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics include assessing the consistency of language models' answers within given spatial constraints.

**Interpretation**: Performance is evaluated based on the ability to predict plausible spatial relations given multiple valid interpretations.

**Baseline Results**: N/A

**Validation**: Evaluated various LLMs, including GPT-4, across different configurations of spatial reasoning tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
