# VisAidMath

## 📊 Benchmark Details

**Name**: VisAidMath

**Overview**: VisAidMath is a benchmark for evaluating the mathematical problem-solving process related to visual information, consisting of 1,200 challenging problems across various mathematical branches and difficulty levels.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MathVista

**Resources**:
- [Resource](https://arxiv.org/abs/2410.22995)

## 🎯 Purpose and Intended Users

**Goal**: To investigate and benchmark the visual-aided reasoning capabilities of large language models and large multimodal models in solving mathematical problems.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual-Aided Reasoning
- Mathematical Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: Collected from a diverse range of educational contexts, including textbooks, examination papers, and mathematical Olympiad problems.

**Size**: 1,200 examples

**Format**: JSON

**Annotation**: Manually annotated through a rigorous data curation pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is evaluated based on the correctness of problem-solving to derive final answers from model outputs.

**Interpretation**: Higher accuracy indicates better performance in visual-aided mathematical reasoning.

**Baseline Results**: N/A

**Validation**: Quality control measures were taken to ensure data reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
