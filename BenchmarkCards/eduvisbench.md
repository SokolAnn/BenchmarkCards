# EduVisBench

## 📊 Benchmark Details

**Name**: EduVisBench

**Overview**: EduVisBench is a multi-domain, multi-level benchmark designed to evaluate the capacity of foundation models to generate pedagogically effective, step-by-step visual reasoning, featuring structured problem sets across diverse domains.

**Data Type**: STEM questions requiring visually grounded solutions

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/aiming-lab/EduVisBench)
- [GitHub Repository](https://github.com/aiming-lab/EduVisAgent)

## 🎯 Purpose and Intended Users

**Goal**: To systematically assess FMs' ability to produce pedagogically effective visualizations for educational purposes.

**Target Audience**:
- ML Researchers
- Educational Professionals
- Model Developers

**Tasks**:
- Visual Reasoning
- Visualization Generation

**Limitations**: N/A

## 💾 Data

**Source**: C-MHChem-Benchmark, high-school-physics dataset, Illustrative Mathematics curriculum, MATH-500 dataset

**Size**: 1,154 STEM questions

**Format**: N/A

**Annotation**: Curated, translated, and adapted for multi-modal visualization tasks

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation using scales

**Metrics**:
- Accuracy
- Context Visualization
- Diagram Design
- Text–Graphic Integration
- Thought Guidance
- Interactivity

**Calculation**: Scores for each metric were assessed using a detailed rubric on a scale of 0 to 5.

**Interpretation**: Higher scores indicate better alignment with pedagogical standards for visual reasoning.

**Baseline Results**: EduVisAgent achieved a score of 81.6% while baseline models scored below 58.2% on average.

**Validation**: Scores were computed based on a fine-grained rubric across multiple visual output dimensions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
