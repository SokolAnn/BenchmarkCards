# MANAGERBENCH

## 📊 Benchmark Details

**Name**: MANAGERBENCH

**Overview**: MANAGERBENCH is a benchmark that evaluates LLM decision-making in realistic, human-validated managerial scenarios, focusing on the safety-pragmatism trade-off in autonomous LLMs' actions.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision
- Healthcare
- Finance
- Legal
- Education
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- HARM-Bench
- MoralBench

**Resources**:
- [GitHub Repository](https://github.com/technion-cs-nlp/ManagerBench)
- [Resource](https://arxiv.org/abs/2510.00857)

## 🎯 Purpose and Intended Users

**Goal**: To expose alignment failures in LLMs and improve the safety and decision-making capabilities in environments where operational goals might conflict with human safety.

**Target Audience**:
- ML Researchers
- Policy Makers
- AI Developers
- Industry Practitioners

**Tasks**:
- Decision Making
- Safety Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Generated via state-of-the-art LLMs and validated by human evaluators.

**Size**: 2,440 examples

**Format**: JSON

**Annotation**: Designed and validated through human assessment for realism and perceived harm.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Harm Avoidance
- Control Pragmatism
- MB-Score
- Tilt Imbalance

**Calculation**: Scores are computed based on the percentage of times models choose safe actions over harmful ones in a set of deliberately contrived scenarios.

**Interpretation**: Scores indicate how well models prioritize safety versus operational objectives, where higher scores reflect better alignment with safety.

**Baseline Results**: Reported performance of state-of-the-art models included GPT-4o, GPT-5, and others against the benchmark.

**Validation**: Validation involved systematic human assessment to ensure scenario realism and relevance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Ethical Decision Making
- Alignment

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Human harm assessments in operational scenarios', 'Overly safe decision making leading to inefficiencies']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
