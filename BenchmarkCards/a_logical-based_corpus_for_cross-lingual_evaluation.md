# A logical-based corpus for cross-lingual evaluation

## 📊 Benchmark Details

**Name**: A logical-based corpus for cross-lingual evaluation

**Overview**: A new synthetic dataset of structure-oriented contradiction detection (CD) tasks designed to isolate structural (logical and syntactic) inference phenomena (Boolean coordination, quantifiers, definite description, counting operators). The dataset is generated from a formal template language and realised in English and Portuguese to (i) compare NLI accuracy of different deep learning models, (ii) diagnose structural competence, and (iii) verify cross-lingual performance.

**Data Type**: text (premise-hypothesis sentence pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Portuguese

**Similar Benchmarks**:
- SNLI
- MNLI
- SciTail
- FraCas
- RTE
- SICK
- Dialogue NLI
- XNLI

**Resources**:
- [GitHub Repository](https://github.com/felipessalvatore/CLCD)
- [GitHub Repository](https://github.com/google-research/bert/blob/master/multilingual.md)
- [GitHub Repository](https://github.com/huggingface/pytorch-pretrained-BERT)

## 🎯 Purpose and Intended Users

**Goal**: Compare the NLI accuracy of different deep learning models on structure-oriented contradiction detection tasks; diagnose the structural (logical and syntactic) competence of each model; verify cross-lingual performance between English and Portuguese.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Natural Language Inference
- Contradiction Detection

**Limitations**: Dataset is synthetic and generated from templates; focuses on isolated structural operators and simple sentence constructions (complex sentences are not covered and are listed as a future direction).

## 💾 Data

**Source**: Automatically generated synthetic premise-hypothesis pairs using a formal template language; realizations provided in English and Portuguese. Full dataset, generation code and templates are available at the project's GitHub repository.

**Size**: Per task: 10,000 training examples and 1,000 test examples (for each language, as stated: "For each task, we provide training and test data with 10K and 1K examples, respectively").

**Format**: N/A

**Annotation**: Automatically generated labels via formal logical/template rules (no manual annotation described).

## 🔬 Methodology

**Methods**:
- Automated evaluation using a Random Forest baseline with Bag-of-Words representation
- Recurrent Neural Networks (RNN, LSTM, GRU) including bidirectional variants
- Transformer-based model: BERT (fine-tuning of pre-trained models, including English BERT, Multilingual BERT, and Chinese BERT)
- Cross-lingual transfer experiments and controlled data modifications (vocabulary intersection, noise label, premise-only, hypothesis-only)

**Metrics**:
- Accuracy

**Calculation**: Accuracy on held-out test data (test sets are balanced). Models are trained on provided training splits (per task: 10K examples) and evaluated on the corresponding 1K test examples; accuracy reported as percentage.

**Interpretation**: Higher Accuracy indicates better ability to detect structural contradictions. Near 100% accuracy (e.g., Tasks 1, 2, 4 with BERT) indicates the task is effectively solved by the model; accuracy close to random (~50%) indicates failure to capture structural inference. Improvements with increased training data indicate better generalization.

**Baseline Results**: Reported test accuracy (percent) averages from Table 2: English averages - Base: 53.9, RNN: 55.4, GRU: 58.0, LSTM: 56.2, BERT: 96.1. Portuguese averages - Base: 54.4, RNN: 52.6, GRU: 57.6, LSTM: 52.6, BERT: 91.4. Per-task accuracies for each model are provided in Table 2 of the paper.

**Validation**: Validation via held-out test sets with disjoint realization functions (rtrain and rtest disjoint vocabularies). Additional experiments: (ii) full train/test vocabulary intersection; (iii) cross-lingual fine-tuning with different pre-trained BERTs; (iv) robustness checks using noise label, premise-only, and hypothesis-only versions to detect dataset bias or memorization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
