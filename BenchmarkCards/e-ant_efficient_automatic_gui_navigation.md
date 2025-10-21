# E-ANT (Efficient Automatic GUI NavigaTion)

## 📊 Benchmark Details

**Name**: E-ANT (Efficient Automatic GUI NavigaTion)

**Overview**: The E-ANT dataset is the first large-scale Chinese dataset for GUI navigation that contains real human behavior and high-quality screenshots with annotations, including over 40,000 user operation trajectories across more than 20,000 distinct tiny apps and URLs.

**Data Type**: user operation trajectories

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- Android in the Wild (AitW)

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating GUI navigation and LLM/MLLM decision-making capabilities, specifically in the context of Chinese mobile applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- UI Navigation

**Limitations**: The data is annotated in an environment that may not fully represent real mobile device interactions.

## 💾 Data

**Source**: Collected from diverse tiny-apps, which are lightweight and simple to develop mobile applications.

**Size**: over 40,000 trajectories

**Format**: JSON

**Annotation**: Annotated through interactions of human annotators with the GUI.

## 🔬 Methodology

**Methods**:
- Zero-shot inference
- Fine-tuning
- Fine-tuning with data augmentation

**Metrics**:
- Picture-level Accuracy
- Trajectory-level Accuracy

**Calculation**: Metrics are calculated based on the congruence between model decisions and observed actions in the dataset.

**Interpretation**: Higher accuracy indicates better performance in navigating GUI tasks.

**Baseline Results**: Baseline results are reported for various models tested on the dataset.

**Validation**: The dataset was validated through extensive testing of mainstream models under different strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes a diverse array of tiny apps from different developers, indicating variety in design logic and styles.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
