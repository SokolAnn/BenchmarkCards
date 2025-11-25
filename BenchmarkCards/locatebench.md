# LocateBench

## 📊 Benchmark Details

**Name**: LocateBench

**Overview**: LocateBench is a high-quality benchmark dedicated to evaluating the ability of Vision Language Models (VLMs) to locate objects in an image according to natural language instructions. It consists of a multiple choice question dataset where VLMs must select the correct bounding box from four candidates based on the provided questions.

**Data Type**: multiple-choice questions with bounding boxes

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Pointing QA

**Resources**:
- [Resource](https://usc-tamagotchi.github.io/locate-bench/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of LocateBench is to evaluate VLMs' ability to locate objects specified by natural language descriptions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Object Localization

**Limitations**: The benchmark focuses on multi-choice problems with only four candidates, which may not fully reflect the complexity of some real-world tasks.

## 💾 Data

**Source**: Constructed based on the RefCOCO series datasets using object descriptions from the COCO dataset.

**Size**: 1,317 examples

**Format**: multiple-choice question format

**Annotation**: Expert-annotated descriptions converted to fluent English which-questions without crowdworkers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the correct identification of the bounding box by VLMs from the provided options.

**Interpretation**: Higher accuracy indicates better model performance in locating objects as instructed by natural language.

**Baseline Results**: Human accuracy: 95%. GPT-4o accuracy: significantly lower than human performance.

**Validation**: Rigorous validation process involving manual inspection and correction of examples by authors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
