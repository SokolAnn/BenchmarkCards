# CyPortQA

## 📊 Benchmark Details

**Name**: CyPortQA

**Overview**: CyPortQA is the first multimodal benchmark tailored to port operations under cyclone threat, consisting of 2,917 real-world disruption scenarios and 117,178 structured question-answer pairs aimed at enhancing preparation for tropical cyclones.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating multimodal large language models in the context of cyclone preparedness in port operations.

**Target Audience**:
- ML Researchers
- Disaster Management Practitioners
- Port Operations Stakeholders

**Tasks**:
- Situation Understanding
- Impact Estimation
- Decision Reasoning

**Limitations**: Constructed from U.S.-based tropical cyclone cases; applicability to different cyclone patterns and port operations is untested.

## 💾 Data

**Source**: Data assembled from NOAA tropical cyclone products, port operational impact records, and USCG port-condition bulletins.

**Size**: 2,917 scenarios, 117,178 QA pairs

**Format**: JSON

**Annotation**: Automated generation via a pipeline of curated QA templates based on expert-validated scenarios.

## 🔬 Methodology

**Methods**:
- Automated QA generation
- Evaluation of multimodal understanding and reasoning
- Performance benchmarking

**Metrics**:
- Accuracy

**Calculation**: Proportion of MLLM responses matching the ground-truth answer for closed-ended questions; tolerance-based accuracy for open-ended numeric outputs.

**Interpretation**: Accuracy signifies how well MLLMs understand and respond to cyclone-related port preparedness scenarios.

**Baseline Results**: Results vary across models; proprietary models outperform open-source counterparts.

**Validation**: Cross-validated against expert reviews on a random sample of scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential misinterpretation of cyclone impacts could lead to inadequate preparation and response.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
