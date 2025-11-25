# E-SyncVidStory (E-commerce Synchronized Video Storytelling)

## 📊 Benchmark Details

**Name**: E-SyncVidStory (E-commerce Synchronized Video Storytelling)

**Overview**: The E-SyncVidStory dataset supports the task of Synchronized Video Storytelling, which generates synchronized narrations for videos using rich annotations and a structured storyline.

**Data Type**: video clips with synchronized narration

**Domains**:
- Natural Language Processing
- Computer Vision
- Advertising

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/alibaba/alimama-video-narrator)

## 🎯 Purpose and Intended Users

**Goal**: To explore the task of synchronized video storytelling, providing a dataset and framework to generate coherent video narrations.

**Target Audience**:
- ML Researchers
- Advertisers
- Content Creators

**Tasks**:
- Video Storytelling
- Content Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from high-quality advertisement videos with associated product information.

**Size**: 6,032 videos, 41,292 video clips

**Format**: N/A

**Annotation**: Automatic speech recognition corrections, GPT-based refinement, and manual checks.

## 🔬 Methodology

**Methods**:
- Fine-tuning of large language models (LLMs)
- Evaluation of generated narrations using NL metrics

**Metrics**:
- BLEU Score
- METEOR
- CIDEr

**Calculation**: Metrics are calculated based on generated stories compared to reference narrations, including both automatic and human evaluations.

**Interpretation**: Higher scores in evaluation metrics indicate better performance in generating coherent and engaging narratives.

**Baseline Results**: Compared against existing models like LLaV A and Video-ChatGPT, showing superior performance in generating coherent narrations.

**Validation**: Automatic and human evaluations affirm the quality and coherence of generated stories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential perpetuation of biases in generated narratives']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Automatically generated content from video data which is anonymized to avoid personal identifiers.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data collected conforms to copyright regulations, avoiding identifying individual data.
