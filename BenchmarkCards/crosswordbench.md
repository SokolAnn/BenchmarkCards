# CrossWordBench

## 📊 Benchmark Details

**Name**: CrossWordBench

**Overview**: CrossWordBench is a benchmark designed to evaluate the reasoning capabilities of both LLMs and LVLMs through the medium of crossword puzzles, integrating text-based clues and visual constraints. It allows for the dynamic generation of puzzles in text and image formats and supports adjustable difficulty levels and various evaluation strategies.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/SeanLeng1/CrossWordBench)
- [Resource](https://huggingface.co/datasets/HINT-lab/CrossWordBench)

## 🎯 Purpose and Intended Users

**Goal**: To effectively evaluate the multimodal reasoning capabilities of LLMs and LVLMs using crossword puzzles that integrate both textual and visual constraints.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering
- Reasoning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Puzzles generated from a controllable framework leveraging multilingual word-clue pairs, dictionary definitions, and adapted question-answer pairs from existing benchmarks like CommonsenseQA.

**Size**: 200 puzzles

**Format**: JSON, Image

**Annotation**: Automatically generated through a pipeline that controls puzzle difficulty and structural integrity.

## 🔬 Methodology

**Methods**:
- Zero-shot Chain-of-Thought (CoT) prompting
- Interactive evaluation mode
- Automated metrics

**Metrics**:
- Word Coverage Rate (WCR)
- Letter Coverage Rate (LCR)
- Intersection Consistency Rate (ICR)

**Calculation**: WCR measures word-level accuracy by calculating the percentage of correctly solved words; LCR evaluates letter-level accuracy; ICR measures the internal consistency of answers at intersections.

**Interpretation**: Higher values in WCR, LCR, and ICR indicate better performance in solving crossword puzzles while adhering to structural constraints.

**Baseline Results**: Includes performance comparisons across 20 evaluated models, highlighting reasoning models like o3-mini and DeepSeek-R1.

**Validation**: Extensive evaluation across multiple model architectures, comparing performance on 7x7 and 14x14 grids.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: ['Current models exhibit performance disparities, particularly in grid-parsing accuracy affecting LVLMs.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
