# FedSecurity

## 📊 Benchmark Details

**Name**: FedSecurity

**Overview**: FedSecurity is an end-to-end benchmark that serves as a supplementary component of the FedML library for simulating adversarial attacks and corresponding defense mechanisms in Federated Learning (FL). It contains two key components: FedAttacker, which conducts a variety of attacks during FL training, and FedDefender, which implements defensive mechanisms to counteract these attacks.

**Data Type**: image, text, question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Healthcare
- Finance

**Similar Benchmarks**:
- Blades
- FederatedScope
- FedML

**Resources**:
- [GitHub Repository](https://github.com/FedML-AI/FedML/tree/master/python/fedml/core/security)
- [Resource](https://arxiv.org/abs/2306.04959)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized, end-to-end benchmark for simulating and evaluating adversarial attacks and corresponding defense mechanisms in Federated Learning and federated LLMs, enabling benchmarking of attacks and defenses, flexible configuration and customization, and support for various models and FL optimizers.

**Target Audience**:
- Research community
- Users of FedML

**Tasks**:
- Image Classification
- Text Classification
- Question Answering

**Limitations**: FedSecurity does not support asynchronous federated learning and vertical federated learning yet.

## 💾 Data

**Source**: Datasets used in evaluations include CIFAR10, CIFAR100, FEMNIST, Shakespeare, 20News, PubMedQA, and MNIST; FedLLM and Pythia-1B are used for federated LLM evaluations.

**Size**: PubMedQA: 212,269 questions; sizes for other datasets not specified in the paper.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Simulation with FedML (automated experiments)
- Real-world deployment on edge devices (Theta Network)
- Automated metrics evaluation

**Metrics**:
- Accuracy
- Test Loss

**Calculation**: Evaluated using the global model test Accuracy; for LLM evaluations (Pythia-1B) results are evaluated using Test Loss as reported in the experiments.

**Interpretation**: Defense effectiveness is measured by closeness of test Accuracy to the no-attack (benign) baseline; an effective defense yields Accuracy close to the benign case. Increases in Test Loss indicate adversarial impact.

**Baseline Results**: Baseline scenarios used: no-attack (benign) scenario and original attack scenario without defense. Specific numeric baseline values are not provided in the paper.

**Validation**: Validated via experiments across multiple datasets and models (Exp 1-Exp 6), scaling client counts (Exp 5), federated LLMs (Exp 8-Exp 9), and a real-world edge-device deployment (Exp 10).

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Privacy**: Reidentification
- **Robustness**: Data poisoning, Extraction attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Model integrity compromise (model poisoning and backdoors)', 'Information leakage via training data reconstruction', 'Backdoor-induced misclassification']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
