# Movie101v2: Improved Movie Narration Benchmark

## 📊 Benchmark Details

**Name**: Movie101v2: Improved Movie Narration Benchmark

**Overview**: Movie101v2 is a large-scale, bilingual dataset designed for automatic movie narration generation, enhancing data quality and addressing limitations found in prior datasets.

**Data Type**: bilingual video-narration pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- Movie101

**Resources**:
- [Resource](https://movie101-dataset.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To advance the development of automatic movie narration generation, aimed particularly at assisting visually impaired audiences.

**Target Audience**:
- Research Community
- AI Developers
- Accessibility Advocates

**Tasks**:
- Movie Narration Generation

**Limitations**: N/A

## 💾 Data

**Source**: Xigua Video and automatic speech recognition techniques combined with expert models.

**Size**: 46,000 bilingual video-narration pairs

**Format**: JSON

**Annotation**: Refined using various models and human verification for quality control.

## 🔬 Methodology

**Methods**:
- Baseline evaluation with state-of-the-art Large Vision-Language Models (LVLMs)
- Human evaluation metrics for narrative quality assessment

**Metrics**:
- L1-Score
- L2-Score
- CIDEr
- BLEU
- ROUGE

**Calculation**: L1-Score evaluates the accuracy of visual fact descriptions; L2-Score assesses narrative coherence regarding plot.

**Interpretation**: Scores indicate how well the model-generated narrations align with the expected narrative quality, focusing on visual facts and plot narration.

**Baseline Results**: Performance evaluated using multiple LVLMs including GPT-4V, with varying success across models.

**Validation**: Results verified through human evaluators and comparison against reference narrations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: The dataset is predominantly Chinese, which may introduce cultural biases.

**Potential Harm**: ['Inaccessible narrations for non-Chinese speakers']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information included; care taken to avoid sensitive content.

**Data Licensing**: Dataset released under restrictive permissions for academic use only.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data collection complied with relevant regulations.
