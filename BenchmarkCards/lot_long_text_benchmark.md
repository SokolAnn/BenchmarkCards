# LOT (Long Text Benchmark)

## 📊 Benchmark Details

**Name**: LOT (Long Text Benchmark)

**Overview**: LOT is a story-centric benchmark for evaluating Chinese long text understanding and generation, consisting of two understanding tasks and two generation tasks. It focuses on commonsense reasoning, controllability, and modeling inter-sentence relations and global discourse structures.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/thu-coai/LOT-LongLM)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating the capabilities of models in understanding and generating long Chinese texts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Cloze Test
- Sentence Position Prediction
- Plot Completion
- Outline-conditioned Generation

**Limitations**: N/A

## 💾 Data

**Source**: Human-written Chinese stories collected from public web resources.

**Size**: 2,427 stories processed for the tasks

**Format**: N/A

**Annotation**: Manual annotation by a commercial team led by a professional screenwriter.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- BLEU-1
- BLEU-2

**Calculation**: Metrics are computed based on the outputs of models compared to ground truth.

**Interpretation**: Higher scores indicate better model performance in terms of understanding and generating coherent long-form texts.

**Baseline Results**: Comparison against pre-trained models like BERT and GPT2.

**Validation**: Extensive experiments and human evaluations for task performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
