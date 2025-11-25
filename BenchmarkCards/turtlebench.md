# TurtleBench

## 📊 Benchmark Details

**Name**: TurtleBench

**Overview**: TurtleBench is a dynamic evaluation benchmark that collects real user guesses from an online Turtle Soup Puzzle game, assessing the reasoning capabilities of large language models (LLMs) without relying on external knowledge bases. The dataset includes 1,532 annotated entries.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMLU
- ARC
- MT-Bench

**Resources**:
- [GitHub Repository](https://github.com/mazzzystar/TurtleBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable evaluation benchmark for assessing LLM reasoning capabilities in natural language understanding and logical reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Real user guesses collected from the Turtle Soup Puzzle game.

**Size**: 1,532 examples

**Format**: CSV

**Annotation**: Manual annotation by annotators who categorized guesses as Correct, Incorrect, or Unknown.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy is calculated as the ratio of correct answers to total answers; F1 Score is computed based on the true positives, false positives, and false negatives.

**Interpretation**: Higher scores indicate better reasoning capabilities of the evaluated models.

**Baseline Results**: Claude-3.5-Sonnet and GPT-4o achieved accuracy above 87% in evaluations.

**Validation**: Dataset was validated by manual checks of user guesses against established answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
