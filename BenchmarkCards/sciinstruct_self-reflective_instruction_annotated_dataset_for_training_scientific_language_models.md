# SciInstruct (Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models)

## 📊 Benchmark Details

**Name**: SciInstruct (Self-Reflective Instruction Annotated Dataset for Training Scientific Language Models)

**Overview**: SciInstruct is a comprehensive dataset designed to enhance the scientific reasoning capabilities of large language models (LLMs) by providing a rich collection of scientific instructions across physics, chemistry, and mathematics, along with a novel self-reflective annotation framework to address data scarcity in science.

**Data Type**: scientific instruction pairs (question-answer pairs)

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- Galactica
- MathInstruct
- MetaMath

**Resources**:
- [GitHub Repository](https://github.com/THUDM/SciGLM)
- [Resource](https://huggingface.co/datasets/zd21/SciInstruct)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the SciInstruct dataset is to improve the scientific problem-solving capabilities of LLMs by providing detailed reasoning instructions that cover various scientific domains.

**Target Audience**:
- ML Researchers
- Model Developers
- Educators

**Tasks**:
- Scientific Reasoning
- Mathematical Problem Solving
- Conceptual Understanding in Science

**Limitations**: The effectiveness of SciInstruct is still constrained by the model’s scale and the inherent difficulty of scientific reasoning tasks.

## 💾 Data

**Source**: Curated from a variety of educational materials, including textbooks and problem sets from physics, chemistry, and mathematics.

**Size**: 254,051 instructions

**Format**: JSON

**Annotation**: Automatically annotated using a self-reflective framework, with filtering for quality using a data classifier.

## 🔬 Methodology

**Methods**:
- Self-Reflective Annotation
- Automated Quality Filtering
- Fine-tuning on pre-trained LLMs

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on the performance of models fine-tuned on the dataset against various benchmarks.

**Interpretation**: Higher accuracy indicates better scientific reasoning and problem-solving capabilities of the trained models.

**Baseline Results**: Outperformed existing models like Galactica and MAmmoTH, improving accuracy on scientific reasoning tasks.

**Validation**: Validation through testing on public scientific benchmarks such as CEval-Sci and SciBench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The dataset includes diverse problem types across various domains, aiming to promote inclusivity in scientific education.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
