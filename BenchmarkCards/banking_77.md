# BANKING 77

## 📊 Benchmark Details

**Name**: BANKING 77

**Overview**: A fine-grained single-domain intent detection dataset in the banking domain comprising 13,083 annotated examples across 77 intents, released to facilitate research on intent detection, especially in few-shot setups.

**Data Type**: text (customer service query utterances)

**Domains**:
- Natural Language Processing
- Banking

**Languages**:
- English

**Similar Benchmarks**:
- HWU 64
- CLINC 150
- SNIPS
- Web Apps
- Ask Ubuntu
- Chatbot Corpus

**Resources**:
- [GitHub Repository](https://github.com/PolyAI-LDN/polyai-models)
- [Resource](https://tfhub.dev/google/universal-sentence-encoder-multilingual-large/1)
- [Resource](https://arxiv.org/abs/2003.04807)

## 🎯 Purpose and Intended Users

**Goal**: Provide a challenging fine-grained single-domain intent detection dataset in the banking domain to evaluate intent detectors, with emphasis on few-shot scenarios.

**Target Audience**:
- ML Researchers
- Conversational system developers
- Industry Practitioners

**Tasks**:
- Intent Detection
- Text Classification

**Limitations**: Some intent categories partially overlap, requiring fine-grained decisions and making the dataset more challenging.

## 💾 Data

**Source**: Collected customer service queries in the banking domain and labeled to create the BANKING 77 dataset (single-domain).

**Size**: 13,083 examples

**Format**: N/A

**Annotation**: Labeled with intent labels (77 intents).

## 🔬 Methodology

**Methods**:
- Automated metrics (Accuracy)
- Model-based evaluation (comparisons of pretrained encoders and fine-tuned BERT)
- Few-shot experimental setups (10 and 30 examples per intent)

**Metrics**:
- Accuracy
- Encoding speed (sentences per second)
- Training and evaluation time (seconds)

**Calculation**: Accuracy computed as percentage of correctly classified intents on standard test sets; some experiments report avg, max, and min across hyperparameter runs. Encoding speed reported as average sentences encoded per second; training/evaluation time reported in seconds.

**Interpretation**: Higher accuracy indicates better intent classification. Authors report absolute improvements over baselines (e.g., USE+CONVE RT improves over BERT-TUNED by +1.77 percentage points on BANKING 77 with 10 examples per intent). Faster encoding speed and lower training/evaluation time indicate greater resource efficiency.

**Baseline Results**: Example results (Accuracy %): BANKING 77 (10-shot): BERT-TUNED 83.42, USE 84.23, CONVE RT 83.32, USE+CONVE RT 85.19 (from Table 3).

**Validation**: Used standard test sets for each dataset. Few-shot training subsets were sampled from full data and these training subsets are released for reproducibility.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
