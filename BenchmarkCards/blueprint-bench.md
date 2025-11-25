# Blueprint-Bench

## 📊 Benchmark Details

**Name**: Blueprint-Bench

**Overview**: Blueprint-Bench is a benchmark designed to evaluate spatial reasoning capabilities in AI models through the task of converting apartment photographs into accurate 2D floor plans.

**Data Type**: image

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AndonLabs/Blueprint-Bench-generation)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of Blueprint-Bench is to measure the spatial intelligence of models that are not specifically trained for spatial reasoning tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Spatial Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: The dataset contains 50 apartments, each with approximately 20 images of the interior, alongside ground truth floor plans adapted from official listings.

**Size**: 1,000 images

**Format**: Image files

**Annotation**: Images were annotated based on strict formatting rules for floor plans.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Similarity score based on room connectivity graphs
- Size rankings

**Calculation**: Scores are calculated based on the similarity between generated and ground-truth floor plans by evaluating room connectivity, size rank, and other components.

**Interpretation**: A score of 1 indicates a perfect match, while a score of 0 indicates no similarity.

**Baseline Results**: Human performance serves as a baseline, with AI models typically performing at or below a random baseline.

**Validation**: Blueprint-Bench will continue to be updated with new models and community submissions for ongoing evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
