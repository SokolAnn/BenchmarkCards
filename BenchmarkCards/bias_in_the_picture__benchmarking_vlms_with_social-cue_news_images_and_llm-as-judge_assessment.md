# Bias in the Picture: Benchmarking VLMs with Social-Cue News Images and LLM-as-Judge Assessment

## 📊 Benchmark Details

**Name**: Bias in the Picture: Benchmarking VLMs with Social-Cue News Images and LLM-as-Judge Assessment

**Overview**: We introduce a benchmark constructed from real-world news images paired with open-ended questions, annotated for age, gender, race, occupation, and sport, enabling joint evaluation of both bias and faithfulness in multimodal reasoning.

**Data Type**: image-question pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To systematically audit how visible social cues modulate stereotypes in multimodal LLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Bias Evaluation

**Limitations**: Our dataset is constrained in scale and domain, focusing on news images from a one-year period.

## 💾 Data

**Source**: Images collected from Google News RSS feeds across various topics.

**Size**: 1,343 image-question pairs

**Format**: N/A

**Annotation**: Annotated with demographic and social attributes by trained annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM as judge

**Metrics**:
- Accuracy
- Bias
- Faithfulness

**Calculation**: The rubric scores the models based on Bias (lower is better), Answer Relevance (higher is better), Faithfulness to the image (higher is better).

**Interpretation**: Higher scores indicate better performance.

**Baseline Results**: Various vision-language models were evaluated with scores on accuracy, bias and faithfulness.

**Validation**: Results were validated through human verification.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Annotated across multiple demographic categories.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Removed personally identifiable elements and obtained informed consent from annotators.

**Data Licensing**: Not Applicable

**Consent Procedures**: Annotated with voluntary, informed consent.

**Compliance With Regulations**: Compliant with institutional privacy policies and relevant data regulations.
