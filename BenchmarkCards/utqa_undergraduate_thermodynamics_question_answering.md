# UTQA (Undergraduate Thermodynamics Question Answering)

## 📊 Benchmark Details

**Name**: UTQA (Undergraduate Thermodynamics Question Answering)

**Overview**: UTQA is a 50-item undergraduate thermodynamics question answering benchmark, covering ideal-gas processes, reversibility, and diagram interpretation, aimed at evaluating LLM competence in thermodynamics.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GPQA
- SciBench

**Resources**:
- [Resource](https://huggingface.co/datasets/herteltm/UTQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate large language models' capabilities in reasoning and tutoring in undergraduate thermodynamics.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Developed by experts based on thermodynamics curriculum.

**Size**: 50 items

**Format**: Multiple choice (single-choice)

**Annotation**: Expert-reviewed and tested for clarity and correctness.

## 🔬 Methodology

**Methods**:
- Cross-model benchmark comparison
- Prompting and linguistic degradation experiments

**Metrics**:
- Accuracy

**Calculation**: Mean accuracy calculated across multiple runs.

**Interpretation**: Scores indicate the fraction of correctly answered items.

**Baseline Results**: Top-performing LLMs achieved up to 82% accuracy.

**Validation**: Peer-reviewed methodology and testing across various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
