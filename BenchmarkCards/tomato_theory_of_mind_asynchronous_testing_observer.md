# ToMATO (Theory of Mind Asynchronous Testing Observer)

## 📊 Benchmark Details

**Name**: ToMATO (Theory of Mind Asynchronous Testing Observer)

**Overview**: ToMATO is a new Theory of Mind benchmark formulated as multiple-choice QA over conversations, capturing both first- and second-order mental states in various categories. It addresses limitations in previous benchmarks by incorporating information asymmetry and distinct personality traits.

**Data Type**: multiple-choice question answering

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FANToM
- ToMi
- Hi-ToM
- BigToM
- FauxPas-EAI
- OpenToM
- ToMBench

**Resources**:
- [GitHub Repository](https://github.com/nttmdlab-nlp/ToMATO)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the Theory of Mind capabilities of LLMs through a comprehensive benchmark that includes diverse personality traits and first- and second-order mental states.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Theory of Mind Evaluation
- Question Answering

**Limitations**: ToMATO's performance may vary depending on the personality traits of characters involved in the conversations.

## 💾 Data

**Source**: Generated through LLM-LLM conversations with Inner Speech prompting.

**Size**: 5,400 questions

**Format**: JSON

**Annotation**: Automatically generated via LLM-LLM interaction and validated by human raters.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on the number of correct responses to the questions in ToMATO.

**Interpretation**: Higher accuracy indicates better performance in understanding mental states and responding appropriately.

**Baseline Results**: Performance of various LLMs assessed against human benchmarks.

**Validation**: Quality validated through human annotators and consistency checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: ToMATO ensures diverse personality traits are represented in interactions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
