# TutorQA

## 📊 Benchmark Details

**Name**: TutorQA

**Overview**: TutorQA is a new expert-verified NLP-focused benchmark for scientific graph reasoning and question-answering, consisting of five tasks with 500 QA pairs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LectureBankCD
- FairytaleQA
- ExpertQA

**Resources**:
- [GitHub Repository](https://github.com/IreneZihuiLi/CGPrompt)

## 🎯 Purpose and Intended Users

**Goal**: To assess large language models’ capabilities in educational scenarios, particularly in recovering concept graphs and answering questions effectively.

**Target Audience**:
- ML Researchers
- Educational Institutions
- NLP Practitioners

**Tasks**:
- Prerequisite Prediction
- Path Searching
- Shortest Path Searching
- Concept Advising
- Idea Hamster

**Limitations**: Constructing a concept graph from scratch can be challenging due to the exponential growth in pair combinations as the number of concepts increases.

## 💾 Data

**Source**: Expert-verified question-answering reference pairs generated based on educational concepts and their prerequisites.

**Size**: 500 QA pairs

**Format**: JSON

**Annotation**: Manually verified by domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Similarity-based F1

**Calculation**: Metrics are calculated based on correct predictions and semantic similarity.

**Interpretation**: Higher scores indicate better performance in identifying concept relationships and answering questions.

**Baseline Results**: Comparison with existing benchmarks like LectureBankCD, showing competitive performance.

**Validation**: Performance validation against multiple models including LLaMa and GPT series.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: TutorQA has been expert-verified to ensure it contains no harmful or private information about individuals.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
