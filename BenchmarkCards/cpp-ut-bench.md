# CPP-UT-Bench

## 📊 Benchmark Details

**Name**: CPP-UT-Bench

**Overview**: CPP-UT-Bench is a benchmark dataset to measure C++ unit test generation capability of large language models (LLMs), reflecting a broad and diverse set of C++ codebases found in the real world.

**Data Type**: code-unit test pairs

**Domains**:
- Software Engineering

**Languages**:
- C++

**Resources**:
- [Resource](https://huggingface.co/datasets/Nutanix/CPP-UNITTEST-BENCH)
- [Resource](https://huggingface.co/datasets/Nutanix/cpp_train_dataset_chat_format_less_than_8k)
- [Resource](https://huggingface.co/datasets/Nutanix/CPP-UNITTEST-BENCH/blob/main/data_scrape.py)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CPP-UT-Bench is to evaluate C++ unit test generation using advanced LLMs for few-shot in-context learning and fine-tuning.

**Target Audience**:
- ML Researchers
- Software Engineers
- AI Practitioners

**Tasks**:
- Unit Test Generation
- Few-Shot Learning
- Parameter-Efficient Fine-Tuning

**Limitations**: N/A

## 💾 Data

**Source**: Open-source C++ codebases from GitHub

**Size**: 2,653 pairs

**Format**: JSON

**Annotation**: Manual curation of code and unit test pairs

## 🔬 Methodology

**Methods**:
- Few-Shot In-Context Learning
- Parameter-Efficient Fine-Tuning
- Full-Parameter Fine-Tuning

**Metrics**:
- Win Rate

**Calculation**: The percentage of instances where one model’s output is judged to be more closely aligned with ground truth compared to another model’s output.

**Interpretation**: A higher win rate indicates better performance in generating accurate unit tests.

**Baseline Results**: N/A

**Validation**: Evaluated through comparative analysis with existing models on the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
