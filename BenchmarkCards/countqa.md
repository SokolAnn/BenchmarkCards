# CountQA

## 📊 Benchmark Details

**Name**: CountQA

**Overview**: CountQA is a challenging new benchmark designed to probe the deficiencies of Multimodal Large Language Models (MLLMs) in counting objects in complex visual scenes. It comprises over 1,500 question-answer pairs featuring real-world images with high object density, clutter, and occlusion.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ShanghaiTech
- UCF-QNRF
- JHU-CROWD++
- NWPU-Crowd

**Resources**:
- [Resource](https://huggingface.co/datasets/CountQA)

## 🎯 Purpose and Intended Users

**Goal**: To assess the fundamental counting abilities of MLLMs in visually-complex scenarios and promote the development of more spatially aware and numerically grounded models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Object Counting

**Limitations**: The dataset primarily reflects specific residential and public areas and may not encompass the full diversity of objects found globally. The current scope focuses on direct enumeration and simple compositional counting, not more complex forms of numerical reasoning.

## 💾 Data

**Source**: Manually collected images depicting everyday indoor and outdoor scenes.

**Size**: 1,001 images and 1,528 question-answer pairs

**Format**: N/A

**Annotation**: Ground truth counts established in situ during image capture.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- Relaxed Accuracy (RA@5%)
- Relaxed Accuracy (RA@10%)

**Calculation**: EM measures the percentage of predictions where the extracted number matches the ground truth. RA metrics evaluate accuracy within 5% and 10% thresholds.

**Interpretation**: Higher values indicate better model performance. An EM of 100% signifies perfect counts.

**Baseline Results**: The top-performing model, Gemini 2.5 Pro, achieved an EM of 42.9%.

**Validation**: Evaluated under zero-shot conditions using a consistent system prompt for counting tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset will be open-sourced upon paper acceptance.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
