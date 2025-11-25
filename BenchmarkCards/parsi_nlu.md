# PARSI NLU

## 📊 Benchmark Details

**Name**: PARSI NLU

**Overview**: PARSI NLU is the first benchmark in Persian language that includes a range of language understanding tasks, including Reading Comprehension, Textual Entailment, and more. It contains over 14.5k instances across 6 distinct NLU tasks.

**Data Type**: question-answering pairs, textual entailment pairs, sentiment analysis reviews, multiple-choice questions, paraphrase pairs, machine translation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- XNLI

**Resources**:
- [Resource](https://git.io/JIuROe)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality evaluation benchmark for Persian NLU tasks and promote further research on Persian language understanding.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Reading Comprehension
- Multiple-Choice Question Answering
- Textual Entailment
- Aspect-Based Sentiment Analysis
- Question Paraphrasing
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Collected via manual annotations by native Persian speakers and various datasets including literature and online content.

**Size**: 14,500 instances

**Format**: JSON

**Annotation**: Manual annotation by native speakers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the specific needs of each task, such as F1 for reading comprehension and accuracy for sentiment analysis.

**Interpretation**: The results indicate performance gaps between human and machine assessments, showcasing the difficulty of tasks.

**Baseline Results**: mT5 achieved state-of-the-art performance on several tasks, but significant gaps remain compared to human performance.

**Validation**: Each task was validated using inter-annotator agreement metrics to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
