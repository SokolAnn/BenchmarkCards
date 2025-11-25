# A Benchmark for Math Misconceptions: Bridging Gaps in Middle School Algebra with AI-Supported Instruction

## 📊 Benchmark Details

**Name**: A Benchmark for Math Misconceptions: Bridging Gaps in Middle School Algebra with AI-Supported Instruction

**Overview**: This study introduces an evaluation benchmark for middle school algebra that supports AI systems aimed at enhancing learners' conceptual understanding of algebra by considering their current levels of comprehension. It includes 55 algebra misconceptions and 220 diagnostic examples.

**Data Type**: question-answering pairs

**Domains**:
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/creature-ai/math-misconceptions)
- [Resource](https://huggingface.co/datasets/math-misconceptions)

## 🎯 Purpose and Intended Users

**Goal**: To support algebra educators in better identifying misconceptions and errors in the classroom.

**Target Audience**:
- Educators
- Researchers
- AI Practitioners

**Tasks**:
- Misconception Identification
- Diagnostic Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from 145 peer-reviewed journal manuscripts and educator feedback.

**Size**: 220 examples

**Format**: JSON

**Annotation**: Research-based examples generated through analysis of existing literature.

## 🔬 Methodology

**Methods**:
- LLM Performance Evaluation
- Educator Feedback

**Metrics**:
- Precision
- Recall

**Calculation**: Precision and recall scores calculated per Misconception based on the model's classifications.

**Interpretation**: High scores indicate effective identification of misconceptions; lower scores highlight areas needing improvement.

**Baseline Results**: Achieved 83.91% accuracy with topic-constrained testing.

**Validation**: Evaluated through human educator feedback and model performance metrics.

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
