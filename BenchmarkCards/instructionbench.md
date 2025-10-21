# InstructionBench

## 📊 Benchmark Details

**Name**: InstructionBench

**Overview**: InstructionBench is designed to evaluate the temporal reasoning capabilities of Video-LLMs in instructional video scenarios, including 5,000 Q&A pairs across over 700 videos, specifically targeting advanced temporal reasoning within strict step-by-step instructional videos.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- MSRVTT-QA
- TVQA

**Resources**:
- [Resource](https://huggingface.co/datasets/sunwhw/InstructionBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess models' capabilities in understanding and reasoning about instructional videos with a focus on temporal aspects.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Temporal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Combined from YouCook2, HiREST, Ego4D Goal-Step, and Ego-Exo4D datasets.

**Size**: 5,000 questions

**Format**: JSON

**Annotation**: Automatically generated Q&A pairs with filtering to ensure quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on the percentage of correct answers out of total questions evaluated.

**Interpretation**: Higher accuracy indicates better temporal reasoning capabilities of Video-LLMs.

**Validation**: The benchmark was validated through comparisons with performance metrics of existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
