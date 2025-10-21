# WORLD CUISINES

## 📊 Benchmark Details

**Name**: WORLD CUISINES

**Overview**: WORLD CUISINES is a massive-scale benchmark for multilingual and multicultural, visually grounded language understanding. It includes a visual question answering (VQA) dataset with text-image pairs across 30 languages and dialects, spanning 9 language families and featuring over 1 million data points.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Japanese
- French
- Indonesian
- Chinese
- Cantonese
- Korean
- Thai
- Spanish
- Russian
- Arabic
- Turkish
- Bengali
- Hindi
- Marathi
- Tamil
- Vietnamese
- Urdu
- Yoruba
- Persian
- Azerbaijani
- Sundanese
- Javanese
- Hokkien
- Sinhala
- Tagalog
- Kazakh
- Ukrainian
- Swahili
- Czech
- Italian
- German
- Dutch

**Similar Benchmarks**:
- FoodieQA
- World Wide Dishes
- CulturalVQA

**Resources**:
- [Resource](https://huggingface.co/datasets/worldcuisines/vqa)
- [Resource](https://huggingface.co/worldcuisines)
- [GitHub Repository](https://github.com/worldcuisines/worldcuisines)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cultural relevance and understanding of vision-language models (VLMs) within the food domain.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from Wikipedia and Wikimedia Commons.

**Size**: 1,000,000 examples

**Format**: JSON

**Annotation**: Annotated by native speakers and experts, ensuring cultural relevance and accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BERTScore

**Calculation**: Accuracy calculated by comparing model predictions with ground truth labels; BERTScore measures similarity between generated answers and reference answers.

**Interpretation**: Higher accuracy indicates better performance, while BERTScore assesses semantic similarity.

**Validation**: Cross-validation techniques to ensure reliability and validity of the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset covers a wide range of languages and cultural contexts, aiming to improve representation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-SA 4.0

**Consent Procedures**: The study's dataset involved voluntary contributions from native speakers.

**Compliance With Regulations**: Not Applicable
