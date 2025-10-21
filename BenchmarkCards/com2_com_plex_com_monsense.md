# COM2 (COM plex COM monsense)

## 📊 Benchmark Details

**Name**: COM2 (COM plex COM monsense)

**Overview**: COM2 is a complex commonsense reasoning dataset created by sampling multi-hop logical queries from an existing commonsense knowledge graph (CSKG) and verbalizing them into multiple-choice and text generation questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/tqfang/complex-commonsense-reasoning)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating complex commonsense reasoning abilities of language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: Issues with data quality and sparsity affecting query construction.

## 💾 Data

**Source**: Sampled logical queries from the ATOMIC commonsense knowledge graph

**Size**: 790,000 examples

**Format**: JSON

**Annotation**: Manually validated by crowdworkers on Amazon Mechanical Turk

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are computed based on performance on the COM2 evaluation set.

**Interpretation**: Higher accuracy indicates better reasoning capabilities.

**Baseline Results**: DeBERTa-v3 fine-tuned on COM2 achieved a significant improvement in reasoning tasks.

**Validation**: Evaluated through human annotation and comparison with existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Potential demographic biases based on the source dataset (ATOMIC).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
