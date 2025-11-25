# MM-GCoT (Multimodal Grounded Chain-of-Thought)

## 📊 Benchmark Details

**Name**: MM-GCoT (Multimodal Grounded Chain-of-Thought)

**Overview**: MM-GCoT is a dataset designed to alleviate visual hallucinations in multimodal large language models (MLLMs) by enhancing their visual-spatial reasoning capabilities through a new learning task termed Grounded Chain-of-Thought (GCoT). It contains training examples for teaching models to ground their reasoning steps with visual evidence.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DoubtedSteam/MM-GCoT)

## 🎯 Purpose and Intended Users

**Goal**: To promote research on Grounded Chain-of-Thought (GCoT) for multimodal large language models, specifically targeting the reduction of visual hallucination issues through improved visual-spatial reasoning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Question Answering
- Grounding
- Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dataset specifically for training and evaluating visual hallucination in MLLMs.

**Size**: 24,022 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Comparison evaluation

**Metrics**:
- Answer Accuracy
- Grounding Accuracy
- Answer-Grounding Consistency

**Calculation**: Computed based on the comparison of predicted answers and grounding boxes against ground truth.

**Interpretation**: Higher accuracy indicates better performance in visual grounding and reasoning consistency; lower metrics indicate visual hallucinations.

**Baseline Results**: N/A

**Validation**: Extensive evaluation on 12 advanced MLLMs to assess performance under various prompting strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Robustness**: Evasion attack, Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
