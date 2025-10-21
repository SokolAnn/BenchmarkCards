# DialogID : A Dialogic Instruction Dataset for Improving Teaching Effectiveness in Online Environments

## 📊 Benchmark Details

**Name**: DialogID : A Dialogic Instruction Dataset for Improving Teaching Effectiveness in Online Environments

**Overview**: DialogID is a dataset of online dialogic instruction detection that contains 30,431 effective dialogic instructions extracted from real-world K-12 online classes and annotated into 8 categories. It is presented to help and promote research and development of tasks for online dialogic instruction detection and improving online teaching effectiveness.

**Data Type**: multimodal (audio segments and text transcriptions)

**Domains**:
- Education
- Natural Language Processing

**Similar Benchmarks**:
- CLASS
- COPUS

**Resources**:
- [GitHub Repository](https://github.com/ai4ed/DialogID)

## 🎯 Purpose and Intended Users

**Goal**: To help and promote research and development of tasks for online dialogic instruction detection by presenting DialogID, a high-quality dialogic instruction dataset for improving online teaching effectiveness.

**Target Audience**:
- Education technology community
- Educational data mining community

**Tasks**:
- Text Classification
- Dialogic Instruction Detection

**Limitations**: None

## 💾 Data

**Source**: Collected and constructed from the K-12 online classes at TAL Education Group.

**Size**: 51,908 annotated samples; 30,431 effective dialogic instructions. Train: 36,335 samples; Validation: 5,191 samples; Test: 10,382 samples.

**Format**: N/A

**Annotation**: A 3-step annotation process: Step 1 extract teacher utterances using an in-house VAD model; Step 2 transcribe utterances via a self-trained ASR model and generate dialogic instruction candidates via keyword matching; Step 3 assemble candidate utterance with surrounding utterances into audio segments and have crowd workers assign labels after listening to each audio segment.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (pre-trained language models, e.g., RoBERTa, BERT, ELECTRA, MacBERT, XLNet)
- Adversarial training enhanced evaluation (RoBERTa+AT)
- Ablation study (comparison with and without adversarial training)
- Human annotation for ground truth labels

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are computed in terms of precision, recall and F1 scores as reported per instruction type and overall.

**Interpretation**: Higher Precision/Recall/F1 indicate better detection performance. The authors state that RoBERTa achieves the highest prediction performance in terms of F1 score, indicating stronger capacity to model dialogic instructions, and that adding adversarial training (RoBERTa+AT) improves generalization as reflected by higher F1 scores (e.g., a 1.66% F1 increase in greeting).

**Baseline Results**: Overall prediction performance - BERT: Precision 0.8534, Recall 0.9092, F1 0.8795; ELECTRA: Precision 0.8338, Recall 0.9145, F1 0.8720; MacBERT: Precision 0.8534, Recall 0.9064, F1 0.8779; XLNet: Precision 0.8505, Recall 0.8920, F1 0.8701; RoBERTa: Precision 0.8483, Recall 0.9167, F1 0.8802; RoBERTa+AT: Precision 0.8545, Recall 0.9183, F1 0.8849.

**Validation**: Data split into training, validation, and test sets as shown in Table 2. Model training used max_len=128, learning rate=1e-5, up to 100 epochs with early stopping if no validation improvement for 5 epochs. Validation set performance was used for early stopping and model selection.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
