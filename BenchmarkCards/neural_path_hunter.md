# Neural Path Hunter

## 📊 Benchmark Details

**Name**: Neural Path Hunter

**Overview**: Neural Path Hunter (NPH) introduces a refinement strategy for dialogue systems aiming to reduce hallucination in generated responses by utilizing external Knowledge Graphs (KG). It operates by identifying hallucinations and correcting them through a generate-then-refine approach, significantly improving factual accuracy in dialogueresponses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OpenDialKG

**Resources**:
- [GitHub Repository](https://github.com/nouhadziri/Neural-Path-Hunter)

## 🎯 Purpose and Intended Users

**Goal**: To improve the faithfulness and reduce hallucination of neural dialogue systems using a Knowledge Graph.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Dialogue System Developers

**Tasks**:
- Dialogue Generation
- Factual Consistency Assessment

**Limitations**: N/A

## 💾 Data

**Source**: OpenDialKG dataset, which consists of turn-based dialogues containing knowledge triples from a Knowledge Graph.

**Size**: 23,314 training examples, 2,954 validation examples, 2,954 test examples

**Format**: JSON

**Annotation**: The data includes annotated responses based on extracted knowledge triples.

## 🔬 Methodology

**Methods**:
- Human Evaluation
- Automated Metrics
- Model-based Evaluation

**Metrics**:
- F1 Score
- Precision
- Recall
- BLEU Score

**Calculation**: Metrics are calculated based on the performance of the dialogue system before and after applying the Neural Path Hunter, comparing generated outputs against ground truth using various evaluation methods.

**Interpretation**: A higher score in FeQA indicates better factual accuracy in the generated dialogue responses.

**Baseline Results**: N/A

**Validation**: The effectiveness of NPH was validated through experiments on the OpenDialKG dataset, showing improvements in dialogue fidelity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate information generation in dialogue systems leading to user misinformation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
