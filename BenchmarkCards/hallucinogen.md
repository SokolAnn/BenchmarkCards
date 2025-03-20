# HALLUCINOGEN

## 📊 Benchmark Details

**Name**: HALLUCINOGEN

**Overview**: HALLUCINOGEN is a novel visual question answering (VQA) benchmark that employs contextual reasoning prompts as hallucination attacks to evaluate the extent of hallucination in state-of-the-art Large Vision-Language Models (LVLMs). It provides a comprehensive study of the implicit reasoning capabilities of LVLMs by categorizing visual entities into salient and latent entities and designing various hallucination attacks.

**Data Type**: image-prompt pairs

**Domains**:
- vision-language tasks
- medical imaging

**Languages**:
- English

**Similar Benchmarks**:
- POPE
- AMBER
- HallusionBench

**Resources**:
- [Resource](NIH Chest X-ray dataset)
- [Resource](MS-COCO dataset)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate hallucinations in Large Vision-Language Models (LVLMs) and their performance on complex vision-language tasks.

**Target Audience**:
- researchers
- developers in the field of AI
- medical professionals

**Tasks**:
- localization
- visual context reasoning
- counterfactual reasoning

**Limitations**: Current attacks are centered on foundational vision-language tasks such as Visual Question Answering (VQA).

**Out of Scope Uses**:
- general image classification
- simplistic visual recognition tasks

## 💾 Data

**Source**: MS-COCO and NIH Chest X-ray datasets

**Size**: 90,000 image-prompt pairs

**Format**: image-prompt pairs

**Annotation**: Each image is associated with 15 diverse implicit hallucination attack prompts.

## 🔬 Methodology

**Methods**:
- implicit hallucination attacks
- localization prompts
- visual context prompts
- counterfactual reasoning prompts

**Metrics**:
- accuracy
- yes or no response evaluation

**Calculation**: Accuracy is computed based on the proportion of correctly answered questions.

**Interpretation**: Lower accuracy indicates a higher degree of hallucination in the generated responses.

**Baseline Results**: Most LVLMs show performance close to random guessing when tested with HALLUCINOGEN attacks.

**Validation**: Extensive qualitative and quantitative evaluations of eleven LVLMs against hallucination attacks.

## ⚠️ Targeted Risks

**Risk Categories**:
- improper visual inference
- reliability of medical diagnoses
- susceptibility to hallucination

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Decision bias
- **Societal Impact**: Impact on education: bypassing learning, Human exploitation
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset complies with ethical guidelines, ensuring no personal data is included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The study adheres to relevant data protection regulations.
