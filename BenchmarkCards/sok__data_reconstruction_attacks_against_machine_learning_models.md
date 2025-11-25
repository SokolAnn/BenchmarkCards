# SoK: Data Reconstruction Attacks Against Machine Learning Models

## 📊 Benchmark Details

**Name**: SoK: Data Reconstruction Attacks Against Machine Learning Models

**Overview**: This paper addresses the challenges in data reconstruction attacks against machine learning models by proposing a unified taxonomy, formal definitions, and a set of evaluation metrics. It also establishes a benchmark for evaluating reconstruction attacks and provides empirical results to demonstrate the effectiveness of the proposed strategies.

**Data Type**: dataset-level metric, sample-level metric

**Domains**:
- Security
- Privacy

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.15603060)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified framework for data reconstruction attacks, including definitions, metrics, and evaluation methods, enabling better assessment and future research in the field.

**Target Audience**:
- Research community
- Security professionals
- Data privacy researchers

**Tasks**:
- Data Reconstruction
- Privacy Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Multiple benchmarking datasets including CelebA, CIFAR10, and MNIST

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Quantitative evaluation metrics
- Systematic evaluation framework

**Metrics**:
- Fréchet Inception Distance (FID)
- Structural Similarity Index Measure (SSIM)
- Peak Signal-to-Noise Ratio (PSNR)
- Mean Squared Error (MSE)

**Calculation**: Metrics including FID evaluate the distance between reconstructed and target datasets, while SSIM, PSNR, and MSE assess sample-level similarities.

**Interpretation**: Lower FID and MSE values and higher SSIM and PSNR values indicate better reconstruction quality.

**Baseline Results**: N/A

**Validation**: Empirical results from experiments across multiple datasets demonstrate the effectiveness of the proposed methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Security

**Atlas Risks**:
- **Privacy**: Personal information in data, Reidentification
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All experiments conducted using publicly available datasets, ensuring no private data is used.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
