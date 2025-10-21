# VF-E VAL (Video Feedback Evaluation for AI-Generated Content)

## 📊 Benchmark Details

**Name**: VF-E VAL (Video Feedback Evaluation for AI-Generated Content)

**Overview**: VF-E VAL is designed to evaluate the capabilities of multimodal large language models (MLLMs) on generating reliable feedback for AI-generated content (AIGC) videos. It introduces four tasks: coherence validation, error awareness, error type detection, and reasoning evaluation.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/songtingyu/VF-Eval)
- [Resource](https://huggingface.co/datasets/songtingyu/VF-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To advance AIGC video generation processes by evaluating MLLM's feedback on AIGC videos.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Coherence Validation
- Error Awareness
- Error Type Detection
- Reasoning Evaluation

**Limitations**: Only text-to-video models are considered, while videos generated from images may exhibit other types of error cases not addressed in this study.

## 💾 Data

**Source**: A large-scale dataset of AIGC videos generated from diverse prompts across different contexts.

**Size**: 9,740 question-answer pairs

**Format**: N/A

**Annotation**: Annotated by human experts and using MLLMs for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Each task's score is calculated based on models' responses compared to expert annotations.

**Interpretation**: Scores reflect the MLLM's ability to accurately interpret and assess video quality, error types, and reasoning depth.

**Baseline Results**: GPT-4.1 was the best-performing model but still struggled with performance across all tasks.

**Validation**: Human validation process included reviewing and correcting annotations to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
