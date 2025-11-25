# Human-Verified Clinical Reasoning Dataset

## 📊 Benchmark Details

**Name**: Human-Verified Clinical Reasoning Dataset

**Overview**: A highly clinically relevant dataset with 31,247 medical question-answer pairs, each accompanied by expert-validated chain-of-thought (CoT) explanations. This dataset supports the development of medical LLMs capable of transparent and verifiable reasoning, thereby advancing safer and more interpretable AI in medicine.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- EXPERTQA

**Resources**:
- [Resource](https://medbench.opencompass.org.cn/community/data-station)

## 🎯 Purpose and Intended Users

**Goal**: To provide a trustworthy medical AI training and evaluation resource through a dataset curated by combining LLM-generated content and expert validation.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- AI Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset is in Chinese and focused on the context of Chinese medical scenarios.

## 💾 Data

**Source**: Curated from medical examination questions and expanded via LLM-generated content and expert validation.

**Size**: 30,000 QA pairs

**Format**: N/A

**Annotation**: Expert-validated with iterative review involving multiple medical professionals.

## 🔬 Methodology

**Methods**:
- Expert validation
- AI validation
- Human review

**Metrics**:
- Medical correctness
- Reasoning structure
- Information sufficiency
- Terminology clarity
- Clinical value

**Calculation**: Scores are assigned based on a structured rubric across five dimensions.

**Interpretation**: Higher scores indicate better quality of the chain-of-thought explanations.

**Baseline Results**: Models fine-tuned on this dataset outperformed those trained on unvalidated data.

**Validation**: Involved multiple layers of human review and AI validation cycles to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Trustworthiness
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
