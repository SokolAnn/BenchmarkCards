# TCMBench

## 📊 Benchmark Details

**Name**: TCMBench

**Overview**: TCMBench is a comprehensive benchmark for evaluating large language models (LLMs) in the Traditional Chinese Medicine (TCM) domain, featuring the TCM-ED dataset that includes 5,473 questions sourced from the TCM Licensing Exam and introducing TCMScore as a tailored evaluation metric.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/michael-wzhu/ChatMed)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for objectively evaluating the performance of large language models in the domain of Traditional Chinese Medicine.

**Target Audience**:
- ML Researchers
- Domain Experts
- Healthcare Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was constructed from the TCM Licensing Exam, including practice questions that represent the essential knowledge and skills for TCM practitioners.

**Size**: 5,473 question-answering pairs

**Format**: JSON

**Annotation**: Manually selected and reviewed by experts to ensure reliability and comprehensive coverage of TCM branches.

## 🔬 Methodology

**Methods**:
- Accuracy evaluation
- TCMScore evaluation

**Metrics**:
- Accuracy
- TCMScore
- ROUGE
- BertScore
- BartScore

**Calculation**: TCMScore is calculated based on term matching and semantic consistency using a fine-tuned NLI model.

**Interpretation**: Higher scores indicate better performance in understanding and applying TCM knowledge.

**Validation**: Extensive experimental evaluations involving various LLMs in TCM-related question answering tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
