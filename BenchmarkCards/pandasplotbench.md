# PandasPlotBench

## 📊 Benchmark Details

**Name**: PandasPlotBench

**Overview**: This paper introduces the human-curated Pandas-PlotBench dataset, designed to evaluate language models’ effectiveness as assistants in visual data exploration. Our benchmark focuses on generating code for visualizing tabular data—such as a Pandas DataFrame—based on natural language instructions, complementing current evaluation tools and expanding their scope.

**Data Type**: tabular

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MatPlotBench

**Resources**:
- [Resource](https://huggingface.co/datasets/JetBrains-Research/PandasPlotBench)
- [GitHub Repository](https://github.com/JetBrains-Research/PandasPlotBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess AI models as assistants in visual data exploration.

**Target Audience**:
- ML Researchers
- Data Scientists

**Tasks**:
- Code Generation for Data Visualization

**Limitations**: N/A

## 💾 Data

**Source**: Human-curated from the Matplotlib gallery.

**Size**: 175 examples

**Format**: CSV

**Annotation**: Tasks generated with the help of OpenAI GPT-4V.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Visual Score
- Task-based Score

**Calculation**: Scores are calculated based on the adherence of generated plots to task descriptions and visual fidelity.

**Interpretation**: A score of 75 or higher is considered acceptable performance.

**Validation**: Models were evaluated multiple times to ensure robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
