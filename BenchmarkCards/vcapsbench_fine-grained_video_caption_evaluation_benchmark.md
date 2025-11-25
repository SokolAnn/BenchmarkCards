# VCapsBench (Fine-grained Video Caption Evaluation Benchmark)

## 📊 Benchmark Details

**Name**: VCapsBench (Fine-grained Video Caption Evaluation Benchmark)

**Overview**: VCapsBench is the first large-scale fine-grained benchmark for video caption evaluation, comprising 5,677 videos and 109,796 question-answer pairs systematically annotated across 21 dimensions to evaluate video caption quality in text-to-video tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CapsBench

**Resources**:
- [GitHub Repository](https://github.com/GXYM/VCapsBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive video caption evaluation framework that addresses fine-grained aspects of video content necessary for text-to-video generation and enhancements in video understanding.

**Target Audience**:
- ML Researchers
- Video Understanding Researchers

**Tasks**:
- Video Caption Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Composed of videos sourced from ten publicly available datasets including Panda-70M, Ego4D, BDD100K, Pixabay, Pexel, VIDGEN-1M, ChronomicBench, FineVideo, FunQA, and LiFT-HRA-20K.

**Size**: 5,677 videos and 109,796 question-answer pairs

**Format**: N/A

**Annotation**: Multi-dimensional question-answer pairs generated via human correction and LLMs, focusing on video content details.

## 🔬 Methodology

**Methods**:
- Contrastive QA-pairs analysis
- Automated evaluation pipeline leveraging large language models

**Metrics**:
- Accuracy (AR)
- Inconsistency Rate (IR)
- Coverage Rate (CR)

**Calculation**: Metrics are calculated based on LLM responses to generated QA pairs, utilizing classified responses as Positive, Negative, or Unanswerable.

**Interpretation**: Higher AR indicates better caption accuracy, lower IR indicates more consistency in captions, and higher CR signifies greater coverage of relevant content.

**Baseline Results**: Evaluated against various vision-language models (VLMs) including Gemini-2.5-Pro-Preview, GPT-4o, and others.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
