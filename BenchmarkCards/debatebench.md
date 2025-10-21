# DebateBench

## 📊 Benchmark Details

**Name**: DebateBench

**Overview**: DebateBench is a novel dataset consisting of transcripts and metadata from competitive British Parliamentary debates evaluated on their ability to engage in argumentation, deliberation, and alignment with human experts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HellaSwag
- TruthfulQA
- MMLU
- SuperGLUE

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging benchmark for evaluating modern large language models on their reasoning capabilities in long-context argumentation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Speech Scoring
- Speech Ranking
- House Ordering

**Limitations**: N/A

## 💾 Data

**Source**: Transcripts of British Parliamentary debates from prestigious competitive debating tournaments.

**Size**: 256 speeches, approximately 884,395 words

**Format**: N/A

**Annotation**: Annotations include detailed speech-level scores and house rankings sourced from official adjudication data.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Mean Absolute Error (MAE)
- Speaker Score Accuracy

**Calculation**: For ranking tasks, the absolute difference between predicted and ground truth rankings is computed.

**Interpretation**: Lower MAE indicates better performance. A higher accuracy percentage in predicting speaker scores indicates closer alignment with human judges.

**Baseline Results**: Preliminary evaluation shows LLMs struggle on DebateBench, with GPT o1, GPT-4o, and Claude Haiku showing considerable errors.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All speakers provided prior consent for the datasets used.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants gave consent for the use of their speeches in the dataset.

**Compliance With Regulations**: Not Applicable
