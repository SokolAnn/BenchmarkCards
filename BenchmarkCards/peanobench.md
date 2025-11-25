# PeanoBench

## 📊 Benchmark Details

**Name**: PeanoBench

**Overview**: PeanoBench is a human-written dataset derived from the Natural Numbers Game, consisting of 371 Peano Arithmetic proofs, where each natural language proof step is paired with the corresponding logically equivalent tactic in Lean.

**Data Type**: proof pairs

**Domains**:
- Education

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2506.08321)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the LeanTutor system designed to assist students in writing mathematical proofs through formal verification and feedback.

**Target Audience**:
- Educators
- Students
- Educational Researchers

**Tasks**:
- Mathematical Proof Verification
- Educational Feedback Generation

**Limitations**: The dataset includes assumptions such as one-to-one correspondence between natural language proof steps and formal language tactics, which may not scale to more complicated proofs.

## 💾 Data

**Source**: Derived from the Natural Numbers Game, specifically annotated by authors.

**Size**: 371 proofs

**Format**: JSON

**Annotation**: Annotated by authors to create a one-to-one correspondence between natural language proof steps and Lean tactics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Relevance

**Calculation**: Metrics are assessed based on the performance of LeanTutor's system compared to baselines concerning correctness and relevance of feedback provided.

**Interpretation**: Higher scores indicate better performance in feedback accuracy and relevance.

**Baseline Results**: LeanTutor outperformed baseline models with significant improvements in the accuracy and relevance of generated feedback.

**Validation**: Results were validated through human evaluator assessments across multiple proof categories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: The system aims to reduce the potential harm of misguidance by providing feedback that helps students identify specific errors in their reasoning.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache-2.0 license for the original dataset used.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
