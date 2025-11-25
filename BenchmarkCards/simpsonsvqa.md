# SimpsonsVQA

## 📊 Benchmark Details

**Name**: SimpsonsVQA

**Overview**: SimpsonsVQA is a novel dataset for Visual Question Answering derived from The Simpsons TV show, designed to promote inquiry-based learning. It aims to address three scenarios: answering relevant questions, identifying irrelevant questions related to images, and evaluating provided answers as correct, incorrect, or ambiguous.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VQA v1.0
- VQA v2.0
- GQA

**Resources**:
- [Resource](https://simpsonsvqa.org)

## 🎯 Purpose and Intended Users

**Goal**: To enhance interactive and immersive learning through a tailored dataset for visual question answering.

**Target Audience**:
- ML Researchers
- Educators
- Students
- Assistive Technology Developers

**Tasks**:
- Visual Question Answering
- Question Relevance Assessment
- Answer Correctness Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Images from The Simpsons TV show (seasons 24 to 33), generated question-answer pairs via automated methods and manual review.

**Size**: 23,269 images, 166,533 QA pairs

**Format**: N/A

**Annotation**: Automated generation with subsequent manual review for accuracy on Amazon Mechanical Turk

## 🔬 Methodology

**Methods**:
- Human evaluation
- Performance benchmarking with existing VQA models

**Metrics**:
- Accuracy
- Precision
- Recall
- F1-Score

**Calculation**: Metrics calculated based on evaluated performance on test data.

**Interpretation**: Higher scores indicate better model performance on relevant tasks.

**Baseline Results**: N/A

**Validation**: Dataset splits into training, validation, and test sets ensuring robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on education: plagiarism

**Demographic Analysis**: N/A

**Potential Harm**: Stereotyping and bias due to cultural references in The Simpsons show.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
