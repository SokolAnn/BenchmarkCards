# AI4Math (A Native Spanish Benchmark for University-Level Mathematical Reasoning in Large Language Models)

## 📊 Benchmark Details

**Name**: AI4Math (A Native Spanish Benchmark for University-Level Mathematical Reasoning in Large Language Models)

**Overview**: AI4Math is a benchmark of 105 original university-level math problems natively authored in Spanish, spanning seven advanced domains. It aims to evaluate the reasoning capabilities of large language models and highlights the need for native-language benchmarks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish

**Similar Benchmarks**:
- MATH
- GSM8K
- FrontierMath
- MathVista

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning capabilities of large language models in mathematical contexts, specifically for Spanish language.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Mathematical Reasoning

**Limitations**: The benchmark contains 105 problems, which is modest compared to large-scale evaluations.

## 💾 Data

**Source**: Problems were collaboratively authored and reviewed by Latin American STEM students during a structured hackathon.

**Size**: 105 problems

**Format**: N/A

**Annotation**: Each problem comes with an exact answer and a detailed, human-authored step-by-step solution.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Final correctness was determined based solely on the match between the model’s final answer and the ground-truth solution.

**Interpretation**: A model’s success rate is defined as the percentage of problems where the final answer exactly matches the reference solution.

**Baseline Results**: Top models (o3-mini, DeepSeek-R1 685B, DeepSeek-V3 685B) achieve over 70% accuracy.

**Validation**: The evaluation included a comparative analysis of several large language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
