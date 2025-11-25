# Benchmark for Uncertainty & Robustness in Self-Supervised Learning

## 📊 Benchmark Details

**Name**: Benchmark for Uncertainty & Robustness in Self-Supervised Learning

**Overview**: We explore variants of SSL methods for vision and language, train SSL as an auxiliary task for vision and pre-training/fine-tuning for language, then evaluate generalization (in-out classification accuracy) and uncertainty (expected calibration error) across covariate shift datasets (MNIST-C, CIFAR-10-C, CIFAR-10.1, MNLI). Our goal is to create a benchmark with outputs from experiments, providing a starting point for new SSL methods in Reliable Machine Learning.

**Data Type**: image (classification images, corrupted/shifted images), text (sentence-pair natural language inference)

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Uncertainty Baselines
- lebenchmark
- DABS
- Scaling and benchmarking self-supervised visual representation learning

**Resources**:
- [GitHub Repository](https://github.com/hamanhbui/reliable_ssl_baselines)

## 🎯 Purpose and Intended Users

**Goal**: Create a benchmark for a fair comparison between SSL methods in reliable machine learning, including source code, model checkpoints, experiment outputs, and comparing generalization (in-out classification accuracy) and uncertainty (expected calibration error) across covariate shift datasets.

**Target Audience**:
- ML Researchers
- Research community

**Tasks**:
- Image Classification
- Natural Language Inference
- Uncertainty Estimation (Calibration)

**Limitations**: N/A

## 💾 Data

**Source**: MNIST-C, CIFAR-10-C, CIFAR-10.1, MultiNLI (as described in paper)

**Size**: MNIST-C: 10,000 samples; CIFAR-10-C: 10,000 images; CIFAR-10.1: v4 2,021 images, v6 2,000 images; MultiNLI: 433,000 sentence pairs

**Format**: Raw image tensors with dimensions provided (MNIST-C: (1,28,28); CIFAR-10 variants: (3,32,32)); text sentence-pair files for MultiNLI

**Annotation**: Original dataset classification labels (MNIST/CIFAR: 10 classes; MultiNLI: 3 classes: entailment, contradiction, neutral)

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation (NLL, Accuracy, ECE)
- Cross-validation model selection with 10 runs/seeds
- Model evaluation across in-distribution and out-of-distribution test sets

**Metrics**:
- Negative Log Likelihood (NLL)
- Accuracy
- Expected Calibration Error (ECE)

**Calculation**: ECE computed using the deterministic method with the max of predictive softmax as referenced (section 2.1). Metrics are averaged over 10 runs (mean and standard deviation). cNLL/cAccuracy/cECE denote metrics averaged over corruption types for corrupted datasets.

**Interpretation**: Robust generalization measured by in-out classification accuracy (a reliable model is expected to achieve high accuracy in both in- and out-of-distribution). Uncertainty measured by low Expected Calibration Error (ECE); a model is considered reliable if it achieves low ECE in both in-data and out-of-data distributions.

**Baseline Results**: ERM baselines from Table 1: MNIST & MNIST-C ERM NLL 0.0365, Accuracy 98.87%, ECE 0.0107, cNLL 1.5439, cAccuracy 77.64%, cECE 0.1759. CIFAR-10 & CIFAR-10-C ERM NLL 0.9988, Accuracy 86.85%, ECE 0.1115, cNLL 3.4181, cAccuracy 66.22%, cECE 0.2858. MultiNLI (Table 2) BERT NLL 0.5309, Accuracy 0.8242, ECE 0.1546; GPT2 NLL 0.9205, Accuracy 0.5332, ECE 0.04625 (OOD values also reported in Table 2).

**Validation**: For vision tasks, merged raw training and validation then ran tests 10 times with 10 different seeds; for each seed randomly split training and validation (80%/20%), selected model maximizing validation accuracy, and reported mean and standard deviation over 10 runs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Calibration

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Value Alignment**: Over- or under-reliance

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
