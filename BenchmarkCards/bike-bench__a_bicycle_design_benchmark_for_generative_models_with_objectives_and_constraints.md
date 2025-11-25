# Bike-Bench: A Bicycle Design Benchmark for Generative Models with Objectives and Constraints

## 📊 Benchmark Details

**Name**: Bike-Bench: A Bicycle Design Benchmark for Generative Models with Objectives and Constraints

**Overview**: Bike-Bench is an engineering design benchmark for evaluating generative models on problems with multiple real-world objectives and constraints in bicycle design. It quantifies performance characteristics such as aerodynamics, ergonomics, structural mechanics, and human usability, and supports a variety of design generation tasks.

**Data Type**: tabular

**Domains**:
- Engineering Design

**Languages**:
- English

**Resources**:
- [Resource](https://decode.mit.edu/projects/bikebench/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for generative models in constrained multi-objective engineering design problems, specifically bicycle design.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Design Generation

**Limitations**: N/A

## 💾 Data

**Source**: Includes several datasets: 1.4M synthetically-generated bicycle designs, 10K human-sourced ratings of bicycle designs, and additional datasets for cyclist aerodynamics.

**Size**: 1.4 million designs, 10,350 ratings

**Format**: CSV, XML, SVG, PNG

**Annotation**: Human ratings collected through a controlled study and synthetic data generated using a custom pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Validity
- Optimality
- Similarity

**Calculation**: Validity is the proportion of designs satisfying constraints; optimality is calculated using hypervolume; similarity is assessed via Maximum Mean Discrepancy.

**Interpretation**: A model must succeed in all three metrics to demonstrate adequate design capability.

**Validation**: Models are validated against their ability to meet multiple objectives and constraints across various design generations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants provided consent for their data to be used in AI model training and evaluation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent from participants aged 18 or older.

**Compliance With Regulations**: Not Applicable
