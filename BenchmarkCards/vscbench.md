# VSCBench

## 📊 Benchmark Details

**Name**: VSCBench

**Overview**: VSCBench is a novel dataset of 3,600 image-text pairs designed to evaluate safety calibration across image-centric and text-centric scenarios, addressing both undersafety and oversafety in vision-language models (VLMs).

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/jiahuigeng/VSCBench.git)

## 🎯 Purpose and Intended Users

**Goal**: To provide a fine-grained evaluation of model safety calibration and explore strategies to enhance the safety alignment of VLMs.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Safety Calibration

**Limitations**: N/A

## 💾 Data

**Source**: Constructed using a human-LLM collaborative framework, combining visually and textually similar image-text pairs categorized by safety.

**Size**: 3,600 image-text pairs

**Format**: N/A

**Annotation**: Manual verification and curation by human evaluators to ensure safety and relevance.

## 🔬 Methodology

**Methods**:
- Evaluation of safety responses of VLMs
- Supervised fine-tuning methods

**Metrics**:
- Safety response accuracy (SRA)

**Calculation**: SRA scores are calculated based on the proportion of correct responses for safe and unsafe queries.

**Interpretation**: Higher SRA values indicate better safety calibration, with diminishing utility indicating a trade-off in safety measures.

**Baseline Results**: Evaluated across eleven VLMs showing various calibration challenges, including proprietary models like GPT-4.

**Validation**: Extensive evaluation across proprietary and open-weight VLMs to assess safety calibration.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: The dataset includes potentially harmful content to study responses, with precautions in place for ethical considerations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: All annotators provided informed consent and were aware of the study's objectives.

**Compliance With Regulations**: Not Applicable
