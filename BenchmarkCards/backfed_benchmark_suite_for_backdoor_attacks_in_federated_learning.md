# BackFed (Benchmark Suite for Backdoor Attacks in Federated Learning)

## 📊 Benchmark Details

**Name**: BackFed (Benchmark Suite for Backdoor Attacks in Federated Learning)

**Overview**: BackFed is a comprehensive benchmark suite designed to standardize, streamline, and reliably evaluate backdoor attacks and defenses in Federated Learning (FL), focusing on practical constraints.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- FLPoison
- Backdoors101

**Resources**:
- [GitHub Repository](https://github.com/thinh-dao/BackFed)

## 🎯 Purpose and Intended Users

**Goal**: To standardize evaluations of backdoor attacks and defenses in Federated Learning.

**Target Audience**:
- ML Researchers
- Security Practitioners

**Tasks**:
- Image Classification
- Sentiment Analysis
- Next-word Prediction

**Limitations**: N/A

## 💾 Data

**Source**: CIFAR-10, MNIST, FEMNIST, Sentiment140, Reddit Corpus

**Size**: 805,263 samples for FEMNIST, 1,600,498 samples for Sentiment140

**Format**: Various formats including image datasets and text

**Annotation**: Dataset partitioning simulated among clients using Dirichlet and uniform distributions, including artificial simulation of dataset partitioning.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Attack Success Rate (ASR)
- Lifespan

**Calculation**: Evaluation metrics calculated across communication rounds after training completion.

**Interpretation**: Higher values of ASR indicate more effective attacks; Lifespan measures persistence of the backdoor.

**Baseline Results**: Comparison made against existing frameworks like FLPoison.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
