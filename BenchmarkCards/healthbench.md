# HealthBench

## 📊 Benchmark Details

**Name**: HealthBench

**Overview**: HealthBench is an open-source benchmark measuring the performance and safety of large language models in healthcare, consisting of 5,000 multi-turn conversations evaluated through 48,562 unique rubric criteria.

**Data Type**: multi-turn conversations

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- VISTA
- PaperBench
- WildBench
- AMEGA
- MultiChallenge

**Resources**:
- [GitHub Repository](https://github.com/openai/simple-evals)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and extensible standard for evaluating the safety and performance of AI systems in health.

**Target Audience**:
- Researchers
- Healthcare Professionals
- AI Model Developers

**Tasks**:
- Performance Evaluation
- Health-related Conversations Assessment

**Limitations**: N/A

## 💾 Data

**Source**: 5,000 multi-turn conversations generated with input from 262 physicians across 60 countries.

**Size**: 5,000 examples

**Format**: N/A

**Annotation**: Rubrics created by physicians for evaluating model responses.

## 🔬 Methodology

**Methods**:
- Rubric evaluation
- Model-based grading

**Metrics**:
- Accuracy
- Completeness
- Context awareness
- Communication quality
- Instruction following

**Calculation**: Scores are computed based on rubric criteria met by model responses.

**Interpretation**: Scores are interpreted based on performance across different health-related tasks.

**Baseline Results**: Human baseline scores were established where physicians produced responses.

**Validation**: Model responses graded against physician-written rubrics to ensure assessment reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Fairness**
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate medical advice', 'Miscommunication in health interactions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
