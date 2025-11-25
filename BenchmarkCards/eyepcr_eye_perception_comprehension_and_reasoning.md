# EyePCR (Eye Perception, Comprehension and Reasoning)

## 📊 Benchmark Details

**Name**: EyePCR (Eye Perception, Comprehension and Reasoning)

**Overview**: EyePCR is a large-scale benchmark for ophthalmic surgery analysis, assessing cognition across Perception, Comprehension, and Reasoning with over 210k visual question-answering samples, structured clinical knowledge, and fine-grained annotations.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2509.15596)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cognitive abilities of multimodal large language models in the context of clinical reasoning and decision-making within ophthalmic surgery.

**Target Audience**:
- ML Researchers
- Medical Professionals
- AI Practitioners in Healthcare

**Tasks**:
- Perception
- Comprehension
- Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: 2,968 surgical videos from public datasets, curated clinical repositories, and institutional archives.

**Size**: 210,000 VQAs

**Format**: VQA

**Annotation**: Annotated by three senior ophthalmic surgeons for clinical authenticity and reliability.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L

**Calculation**: Simple accuracy for MCQs; BLEU and ROUGE for OEQs.

**Interpretation**: Higher accuracy indicates better model performance in surgical cognition tasks.

**Baseline Results**: EyePCR-MLLM achieves substantial accuracy improvements over Qwen2.5-VL-7B.

**Validation**: Dataset split at the patient level to prevent overlap.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
