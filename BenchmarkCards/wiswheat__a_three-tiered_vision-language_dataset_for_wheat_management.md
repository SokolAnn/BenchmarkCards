# WisWheat: A Three-Tiered Vision-Language Dataset for Wheat Management

## 📊 Benchmark Details

**Name**: WisWheat: A Three-Tiered Vision-Language Dataset for Wheat Management

**Overview**: WisWheat is a wheat-specific dataset with a three-layered design to enhance Vision-Language Models' performance on wheat management tasks, consisting of 47,871 image-caption pairs, 7,263 VQA-style image-question-answer triplets, and 4,888 instruction fine-tuning samples.

**Data Type**: image-caption pairs, image-question-answer triplets

**Domains**:
- Agriculture

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance VLM performance on wheat management applications and provide reliable management recommendations based on wheat-specific data.

**Target Audience**:
- ML Researchers
- Agricultural Scientists
- Data Scientists

**Tasks**:
- Image Captioning
- Visual Question Answering
- Instruction Following

**Limitations**: The domain knowledge is primarily based on the Australian wheat production system.

## 💾 Data

**Source**: Wheat field images from published datasets and peer-reviewed research under permissive public access licenses.

**Size**: 60,022 samples

**Format**: N/A

**Annotation**: Expert-verified image-question-response pairs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Expert evaluation

**Metrics**:
- Accuracy
- Relevance
- Completeness
- Fluency
- Domain Expertise

**Calculation**: Metrics calculated based on expert evaluations and model responses.

**Interpretation**: Scores reflect the quality and utility of model responses in the context of wheat management.

**Baseline Results**: Accuracy scores of fine-tuned Qwen2.5 VL 7B on wheat stress and growth stage conversation tasks reach 79.2% and 84.6% respectively.

**Validation**: Extensive experimental results validating the effectiveness of the proposed dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
