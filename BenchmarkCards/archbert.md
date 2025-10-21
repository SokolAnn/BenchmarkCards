# ArchBERT

## 📊 Benchmark Details

**Name**: ArchBERT

**Overview**: ArchBERT is a bi-modal model designed for joint learning and understanding of neural architectures and natural languages. This work introduces two new bi-modal datasets (TVHF and AutoNet) for enhancing the training and evaluation of multi-modal systems in architecture-language learning, supported by a novel pre-training strategy called Masked Architecture Modeling (MAM).

**Data Type**: bi-modal pairs of architectural graphs and textual descriptions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/ArchBERT)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate joint understanding and learning of neural architectures and natural languages through the ArchBERT framework and to provide datasets that support this goal.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Architectural Reasoning
- Architecture Clone Detection
- Architectural Question Answering
- Architecture Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Two new datasets TVHF and AutoNet were created by collecting and generating neural architectures and their textual descriptions.

**Size**: Total of 3,636,000 samples across both datasets (TVHF and AutoNet combined).

**Format**: JSON

**Annotation**: Manually annotated for accuracy; automatic generation for negative samples.

## 🔬 Methodology

**Methods**:
- Cross-modal learning using a bi-modal model
- Cosine similarity for embedding matching
- Architecture-oriented reasoning tasks

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics were calculated based on similarity scores and ground truth labels.

**Interpretation**: An accuracy above 70% and F1 scores reflecting the model's effectiveness on architecture and text pairs.

**Validation**: Model performance was validated through comparative tests against multiple baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
