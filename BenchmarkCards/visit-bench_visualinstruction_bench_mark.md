# VisIT-Bench (VisualInsTruction Bench mark)

## 📊 Benchmark Details

**Name**: VisIT-Bench (VisualInsTruction Bench mark)

**Overview**: VisIT-Bench is a benchmark for evaluation of instruction-following vision-language models, consisting of 592 diverse tasks designed for multimodal interactions based on human-authored instruction-conditioned captions. The tasks facilitate a quantitative evaluation of how well models can follow instructions across various scenarios, ranging from recognition to complex reasoning.

**Data Type**: instruction-conditioned caption pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VQAv2
- COCO

**Resources**:
- [Resource](https://visit-bench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dynamic evaluation benchmark for instruction-following vision-language models, with a focus on real-world applications and human-verified reference outputs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Vision-Language Instruction Following
- Text Generation
- Visual Question Answering
- Image Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Human-generated instruction-conditioned captions and reference outputs, curated from various instruction families and image datasets.

**Size**: 592 instances and 1,159 public images

**Format**: N/A

**Annotation**: Crowdsourced annotation by human workers and reference generation from GPT-4.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Comparison against references

**Metrics**:
- Win rate vs. human-verified reference
- Elo ratings

**Calculation**: Metrics are calculated based on human judgments in pairwise comparisons and automated evaluation using GPT-4.

**Interpretation**: Higher win rates against human-verified outputs indicate better model performance in following instructions.

**Baseline Results**: Top-performing model achieved a win rate of 27.4% against GPT-4 references.

**Validation**: Participation is dynamic; models submit predictions for evaluation against held-out test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate output generation leading to misinterpretation of instructions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Images sourced are licensed under Creative Commons guidelines, ensuring respect for original licensing terms.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
