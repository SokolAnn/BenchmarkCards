# WILDIFE VAL

## 📊 Benchmark Details

**Name**: WILDIFE VAL

**Overview**: WILDIFE VAL is a large-scale dataset of 12K real user instructions with diverse, multi-constraint conditions, aimed at benchmarking the instruction-following capabilities of leading LLMs in complex, realistic scenarios.

**Data Type**: constrained generation tasks

**Domains**:
- Natural Language Processing
- Education
- Entertainment
- Creative Writing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- IFEval
- FollowBench
- InfoBench

**Resources**:
- [Resource](https://huggingface.co/datasets/gililior/wild-if-eval)
- [GitHub Repository](https://github.com/gililior/wild-if-eval-code)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of LLMs to follow realistic multi-constrained instructions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Constrained Text Generation
- Instruction Following

**Limitations**: The dataset reflects only the types of tasks that interest the platform users, potentially leading to demographic bias.

## 💾 Data

**Source**: Real user instructions collected from Chatbot Arena.

**Size**: 12,000 instructions

**Format**: N/A

**Annotation**: User-generated instructions were decomposed into constraints for evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- Fraction of constraints fulfilled

**Calculation**: Score is calculated as the relative fraction of fulfilled constraints per task.

**Interpretation**: Higher scores indicate better performance in following constraints.

**Validation**: High agreement with human annotations (75%) and significant correlations with existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset's user instructions may not represent diverse demographic groups due to its sourcing.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
