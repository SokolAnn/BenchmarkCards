# MateInfoUB: A Real-World Benchmark for Testing LLMs in Competitive, Multilingual, and Multimodal Educational Tasks

## 📊 Benchmark Details

**Name**: MateInfoUB: A Real-World Benchmark for Testing LLMs in Competitive, Multilingual, and Multimodal Educational Tasks

**Overview**: This study presents a novel bilingual (English–Romanian) multimodal (text and image) dataset of multiple-choice questions derived from a high-level computer science competition, focusing on benchmarking LLM performance on theoretical programming tasks.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Computer Science Education

**Languages**:
- English
- Romanian

**Similar Benchmarks**:
- HumanEval
- MBPP

**Resources**:
- [Resource](https://huggingface.co/datasets/EHollower/MateInfoUB)
- [Resource](https://mateinfo-ub.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models on a bilingual, multimodal dataset in a competitive educational context.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Multiple Choice Question Answering

**Limitations**: The dataset is limited to the Romanian educational context.

## 💾 Data

**Source**: The dataset is derived from real contest problems used in MateInfoUB, an annual computer science contest for 12th-grade students.

**Size**: 100 multiple-choice questions

**Format**: Text and Image

**Annotation**: Manually written extensive solutions by authors and students for reference.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Percentage of correct answers

**Calculation**: Accuracy was measured by directly comparing model responses against the correct answers from the dataset.

**Interpretation**: Higher accuracy indicates better performance of the LLMs on educational tasks.

**Baseline Results**: Gemini 2.5 Exp achieved 76.7% accuracy on hard problems.

**Validation**: Models were evaluated against the results of students from 2021 to 2024 contests.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset focuses on Romanian high school students and may not generalize to other demographics.

**Potential Harm**: Potential misuse of the dataset for unauthorized LLM training or assessment.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
