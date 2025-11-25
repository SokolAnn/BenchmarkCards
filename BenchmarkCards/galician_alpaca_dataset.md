# Galician Alpaca Dataset

## 📊 Benchmark Details

**Name**: Galician Alpaca Dataset

**Overview**: The paper presents a Galician adaptation of the Alpaca dataset, which consists of 52,000 instructions and demonstrations aimed at enhancing Natural Language Processing for the Galician language.

**Data Type**: instruction-response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Galician

**Resources**:
- [Resource](https://huggingface.co/irlab-udc/alpaca-datagalician)
- [Resource](https://huggingface.co/irlab-udc/cabuxa-7b)
- [GitHub Repository](https://github.com/tloen/alpaca-lora/blob/main/templates/alpaca.json)

## 🎯 Purpose and Intended Users

**Goal**: To enhance NLP for the Galician language through an adapted dataset and fine-tuned language model.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Translation of the Alpaca dataset to Galician using googletranslatepy.

**Size**: 52,000 instructions

**Format**: N/A

**Annotation**: Automatically generated via translation.

## 🔬 Methodology

**Methods**:
- Fine-tuning the model using the adapted dataset

**Metrics**:
- Loss

**Calculation**: Training was conducted for 20 epochs, with loss recorded for each epoch.

**Interpretation**: Lower loss values indicate better model performance.

**Baseline Results**: N/A

**Validation**: Validation set comprises 20% of the dataset held back from training.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
