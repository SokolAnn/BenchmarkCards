# HVSBench (Human Visual System Benchmark)

## 📊 Benchmark Details

**Name**: HVSBench (Human Visual System Benchmark)

**Overview**: HVSBench is a large-scale benchmark designed to assess the alignment between Multimodal Large Language Models (MLLMs) and human visual system (HVS) on fundamental vision tasks that mirror human vision. It consists of over 85K multimodal samples spanning 13 categories and 5 fields related to HVS.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MMBench
- SEED-Bench

**Resources**:
- [Resource](https://jiaying.link/HVSBench/plainable)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the extent to which MLLMs align with the human visual system in tasks that mirror human perception.

**Target Audience**:
- ML Researchers
- Models Developers

**Tasks**:
- Visual Question Answering
- Object Detection
- Saliency Ranking

**Limitations**: N/A

## 💾 Data

**Source**: HVSBench is curated from human visual studies and datasets designed specifically to evaluate various aspects of human visual perception.

**Size**: 85,147 question-answer pairs

**Format**: JSON

**Annotation**: Questions were generated and verified by humans to ensure alignment with human attention and perceptions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Field-adaptive evaluation

**Metrics**:
- Accuracy
- Mean Absolute Error (MAE)
- Root Mean Square Error (RMSE)
- MultiMatch

**Calculation**: Metrics are calculated based on the predictions of MLLMs against human responses in various tasks defined in the benchmark.

**Interpretation**: Higher accuracy indicates better alignment of MLLMs with human visual processing behaviors.

**Baseline Results**: Model performance is compared against human results across multiple vision tasks, showing significant gaps.

**Validation**: The benchmark was validated through extensive evaluations of multiple MLLMs and comparisons with human performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
