# R-Bench

## 📊 Benchmark Details

**Name**: R-Bench

**Overview**: A novel benchmark for evaluating Vision Relationship Hallucination in Large Vision-Language Models (LVLMs), focusing on image-level and instance-level questions regarding relations.

**Data Type**: Questions and Images

**Domains**:
- Visual Comprehension
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- AMBER

**Resources**:
- [GitHub Repository](https://github.com/mrwu-mac/R-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and analyze relationship hallucinations in Large Vision-Language Models.

**Target Audience**:
- Researchers
- Academics
- Developers of AI models

**Tasks**:
- Evaluating hallucinations in LVLMs
- Understanding inter-object relationships in visual data

**Limitations**: Limited to analyzing relationship hallucinations, does not cover all types of hallucinations.

**Out of Scope Uses**:
- Evaluation of LLMs without visual components
- Applications outside of vision-language models

## 💾 Data

**Source**: nocaps validation set (Agrawal et al., 2019)

**Size**: 24,897 questions (11,651 after filtering)

**Format**: Questions with binary answers (Yes/No)

**Annotation**: Questions annotated with positive and negative labels

## 🔬 Methodology

**Methods**:
- Parsing COCO captions into relationship triplets
- Using LLM for generating questions
- Employing GroundingDINO for bounding box and mask identification

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Average results based on multiple random subsets with a 1:1 positive-negative question ratio.

**Interpretation**: Analysis of discrepancies between image-level and instance-level question responses.

**Validation**: Involves benchmarking various existing LVLMs on generated questions

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Governance
- Explainability

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias, Output bias, Decision bias
- **Governance**: Lack of system transparency, Unrepresentative risk testing, Incomplete usage definition, Lack of data transparency
- **Explainability**: Inaccessible training data, Untraceable attribution, Unexplainable output

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Maintained through the use of the nocaps dataset, ensuring no overlap with pre-trained data.

**Data Licensing**: Based on publicly available datasets (nocaps, COCO).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Follows guidelines for data use in research.
