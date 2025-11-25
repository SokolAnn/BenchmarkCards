# DECAPBENCH

## 📊 Benchmark Details

**Name**: DECAPBENCH

**Overview**: DECAPBENCH is a detailed captioning benchmark for evaluating the captioning capabilities of modern vision-language models (VLMs), specifically designed to address hallucination and fine-grained comprehensiveness in image captioning.

**Data Type**: captioning pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMVet
- MMStar

**Resources**:
- [GitHub Repository](https://github.com/MAGAer13/DeCapBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable framework for assessing detailed image captioning capabilities of modern visual language models.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Image Captioning

**Limitations**: N/A

## 💾 Data

**Source**: ImageInWords dataset with 400 high-quality, human-curated public image detailed captions.

**Size**: 400 examples

**Format**: N/A

**Annotation**: Human-annotated with a focus on hyper-detailed and hallucination-free descriptions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- DCS CORE

**Calculation**: DCS CORE evaluates image captions through decomposition into primitive information units, assessing their correctness and comprehensiveness.

**Interpretation**: Higher scores indicate fewer hallucinations and greater detail in image captions.

**Baseline Results**: N/A

**Validation**: Extensive experimentation on multiple visual language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Hallucinations in generated captions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
