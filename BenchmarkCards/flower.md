# Flower

## 📊 Benchmark Details

**Name**: Flower

**Overview**: Flower is a novel federated learning framework designed to support large-scale training on heterogeneous edge devices, facilitating both algorithmic experiments and system-level evaluations. It allows for seamless migration between simulation and real-world deployments, targeting a larger number of clients in federated settings.

**Data Type**: N/A

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- TFF
- PySyft
- FedScale
- LEAF

**Resources**:
- [Resource](https://flower.dev)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive federated learning framework that enables research and experimentation with scalable and heterogeneous client environments.

**Target Audience**:
- Researchers
- Academics
- Industry Practitioners

**Tasks**:
- Federated Learning

**Limitations**: N/A

## 💾 Data

**Source**: Data from federated learning clients including public datasets like CIFAR-10 and Fashion-MNIST.

**Size**: 15M clients

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Federated averaging (FedAvg)
- Fault-Tolerant FedAvg
- FedProx

**Metrics**:
- Accuracy
- Top-1 Accuracy
- Top-5 Accuracy

**Calculation**: Metrics are calculated based on the aggregated results from federated clients after each round of training.

**Interpretation**: Higher accuracy and lower training time indicate better performance of the federated learning framework.

**Baseline Results**: FedAvg and other FL methods compared to traditional centralized training metrics.

**Validation**: Performance validated through extensive experiments on real devices and simulations with varying client conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Flower implements secure aggregation methods to maintain client data privacy.

**Data Licensing**: Apache 2.0 License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
