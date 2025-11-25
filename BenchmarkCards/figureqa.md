# FigureQA

## 📊 Benchmark Details

**Name**: FigureQA

**Overview**: We introduce FigureQA, a visual reasoning corpus of over one million question-answer pairs grounded in over 100,000 images. The images are synthetic, scientific-style figures from five classes (line, dot-line, vertical and horizontal bar, and pie charts). Questions (15 templates) examine relationships between plot elements (e.g., maximum, minimum, area-under-the-curve, smoothness, intersection) and are posed as binary yes/no answers. The corpus includes supplementary data: the numerical data used to generate each figure and bounding-box annotations for all plot elements.

**Data Type**: question-answering pairs grounded in images (scientific-style figure images)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VQA
- CLEVR
- NLVR
- FigureSeer

**Resources**:
- [Resource](https://datasets.maluuba.com/FigureQA)
- [GitHub Repository](https://github.com/Maluuba/FigureQA)
- [GitHub Repository](https://github.com/vmichals/FigureQA-baseline)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale synthetically generated corpus to study visual reasoning and comprehension in machines on scientific-style figures, and to facilitate development of models that intuitively recognize patterns from visual representations of data.

**Target Audience**:
- Research community
- Machine learning researchers
- Model developers

**Tasks**:
- Question Answering
- Visual Reasoning
- Data Extraction (auxiliary: reconstructing numerical data from figures)

**Limitations**: The corpus is synthetic and "may not exhibit the same richness as figures 'in the wild'", which may limit direct transfer to real scientific figures.

## 💾 Data

**Source**: Synthetic figures generated from sampled numerical data using a two-stage process: (1) sample numerical data according to constrained distributions and shape functions, (2) render images using the Bokeh plotting library (with a modified backend to extract bounding boxes). Five figure types: line, dot-line, vertical bar, horizontal bar, pie.

**Size**: Training: 100,000 images with 1.3 million questions; Validation: 20,000 images with over 250,000 questions; Test: 20,000 images with over 250,000 questions; Corpus total: over 1 million question-answer pairs grounded in over 100,000 images.

**Format**: PNG (images, RGB). Supplementary numerical data and bounding-box annotations provided (format not specified).

**Annotation**: Questions generated from 15 predefined templates applied to source numerical data; one yes and one no question generated per applicable template then filtered to balance yes/no answers. Bounding boxes for all plot elements extracted via a modified Bokeh backend. Numerical source data retained and released alongside images.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (training neural baseline models: text-only LSTM, CNN+LSTM, CNN+LSTM on VGG-16 features, Relation Network)
- Automated evaluation using Accuracy on validation and test sets
- Human evaluation (editorial staff baseline on a subset of test set)

**Metrics**:
- Accuracy

**Calculation**: Accuracy is computed as the percentage of correctly answered binary (yes/no) questions on validation and test sets. During training, validation accuracy is measured on one randomly selected validation batch per training step and an exponential moving average with decay 0.9 is kept; early stopping is performed based on this moving average starting from the 100th update.

**Interpretation**: Higher Accuracy indicates better model performance on the question-answering task. The paper uses a human baseline (91.21% on a subset of the test set) as reference; model accuracies (e.g., Relation Network at ~72% test accuracy) indicate a gap to human performance and room for improvement.

**Baseline Results**: Validation/Test accuracies (alternated color scheme): Text-only: 50.01% / 50.01%; CNN+LSTM: 56.16% / 56.00%; CNN+LSTM on VGG-16 features: 52.31% / 52.47%; Relation Network (RN): 72.54% / 72.40%. On a human-evaluated subset (test, alternated color scheme): CNN+LSTM 56.04%, RN 72.18%, Human 91.21%. RN achieves 72.40% and 76.52% on test sets depending on color-scheme/training variant as reported.

**Validation**: Datasets constructed with an 'alternated color scheme' (colors in validation/test are from a disjoint subset relative to training) to test generalization; validation accuracy measured on a randomly selected validation batch per training step and tracked via exponential moving average (decay 0.9) for early stopping. The dataset is balanced per question type for yes/no answers to avoid answer-frequency bias.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
