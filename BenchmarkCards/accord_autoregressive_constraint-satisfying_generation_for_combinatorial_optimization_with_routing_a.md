# ACCORD (Autoregressive Constraint-satisfying generation for COmbinatorial Optimization with Routing and Dynamic attention)

## 📊 Benchmark Details

**Name**: ACCORD (Autoregressive Constraint-satisfying generation for COmbinatorial Optimization with Routing and Dynamic attention)

**Overview**: ACCORD is a framework that encodes combinatorial constraints into an autoregressive text format and uses dynamic LoRA routing to probe an LLM’s end-to-end ability on NP-hard tasks. It is associated with the ACCORD-90k dataset, which covers six NP-hard combinatorial problems, including TSP, VRP, Knapsack, FlowShop, JSSP, and BinPacking.

**Data Type**: text

**Domains**:
- Artificial Intelligence
- Operations Research

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/starjob42/ACCORD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a framework and dataset to investigate the reasoning abilities of LLMs on NP-hard combinatorial optimization tasks.

**Target Audience**:
- ML Researchers
- Operations Researchers
- Practitioners in AI

**Tasks**:
- Combined Optimization
- Combinatorial Optimization

**Limitations**: ACCORD is limited by the LLM's context window, which restricts its applicability to very large instances.

## 💾 Data

**Source**: Synthetic datasets generated using Google OR-Tools, covering tasks like TSP, VRP, Knapsack, Flow Shop, JSSP, and Bin Packing.

**Size**: 90,000 examples

**Format**: CSV

**Annotation**: Automatically generated using problem solvers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Feasibility
- Optimality gap

**Calculation**: Feasibility is calculated as the percentage of generated solutions that satisfy all constraints. Optimality gap is defined as Model Value minus OR-Tools Value over OR-Tools Value, where a lower gap indicates a better solution.

**Interpretation**: Higher feasibility percentages and lower optimality gaps indicate better performance for the model.

**Baseline Results**: ACCORD consistently outperforms prompting methods across all six combinatorial optimization tasks.

**Validation**: Extensive ablation studies demonstrate lower optimality gaps compared to traditional methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Transparency

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**
- **Robustness**
- **Transparency**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
