# VCD (Visual Commonsense Dataset)

## 📊 Benchmark Details

**Name**: VCD (Visual Commonsense Dataset)

**Overview**: VCD is a large-scale dataset containing over 100,000 images and 14 million object-commonsense pairs that bridges the gap between linguistic and visual commonsense by integrating structured relations from ConceptNet with object-level annotations from Visual Genome.

**Data Type**: image-commonsense pairs

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ConceptNet
- Visual Genome

**Resources**:
- [GitHub Repository](https://github.com/NUSTM/VCD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundational resource for discovering and leveraging visual commonsense knowledge in AI systems.

**Target Audience**:
- ML Researchers
- AI Developers
- Vision-Language Researchers

**Tasks**:
- Visual Commonsense Reasoning
- Image Captioning
- Vision-Language tasks

**Limitations**: Due to space constraints, the evaluation of the significance of discovered visual commonsense is relatively simple.

## 💾 Data

**Source**: Combination of Visual Genome and ConceptNet

**Size**: 106,277 images, 14 million object-commonsense pairs

**Format**: JSON

**Annotation**: Manual annotation and alignment of existing triples from Visual Genome and ConceptNet

## 🔬 Methodology

**Methods**:
- Automatic evaluation with CLIP
- Human evaluation with Likert scale

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L

**Calculation**: Metrics calculated using automatic matching scores for seen and unseen commonsense.

**Interpretation**: Higher scores indicate better alignment of generated commonsense with human evaluations.

**Baseline Results**: Compared against GPT-4o and other vision-language models.

**Validation**: Human evaluations confirm the quality and relevance of commonsense triples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
