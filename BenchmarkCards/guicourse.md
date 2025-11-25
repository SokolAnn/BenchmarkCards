# GUICourse

## 📊 Benchmark Details

**Name**: GUICourse

**Overview**: GUICourse is a series of datasets aimed at training visual-based GUI agents using general Vision Language Models (VLMs), focusing on tasks like enhancing OCR and grounding abilities and enriching GUI knowledge.

**Data Type**: question-answering pairs, navigation instructions, webpage screenshots

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MiniWoB++
- Rico
- WebShop

**Resources**:
- [GitHub Repository](https://github.com/RUCBM/GUICourse)

## 🎯 Purpose and Intended Users

**Goal**: To improve the training of visual-based GUI agents by providing comprehensive datasets that enhance OCR, grounding abilities, and GUI knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- GUI Navigation
- Question Answering
- Image-Text Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Annotated dataset derived from real-world GUI interactions and web page data, including online scraping and human verification processes.

**Size**: 10,000,000 samples for GUIEnv, 67,000 samples for GUIAct, and 44,000 single-turn QA pairs for GUIChat.

**Format**: JSON, CSV

**Annotation**: Combination of LLM-based auto-annotation (GPT-4) and human annotation for quality verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Type Exact Match Score
- Step Success Rate
- F1 Score

**Calculation**: Metrics are calculated based on the accuracy of predicted actions and their relation to ground truth actions in defined scenarios.

**Interpretation**: Higher success rates indicate better model performance on the navigation and understanding tasks.

**Baseline Results**: Performance results compared against existing VLMs, showcasing improvements on GUI navigation tasks.

**Validation**: The dataset was validated through manual checks and automated evaluation methods to ensure quality and usability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personally identifiable information is collected; dataset is derived from publicly accessible website screenshots.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
