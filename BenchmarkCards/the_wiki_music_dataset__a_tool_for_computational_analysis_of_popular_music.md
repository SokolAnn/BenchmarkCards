# The Wiki Music dataset: A tool for computational analysis of popular music

## 📊 Benchmark Details

**Name**: The Wiki Music dataset: A tool for computational analysis of popular music

**Overview**: A hand-crafted dataset intended to combine features about style, psychology, sociology and typology, annotated by music genre and indexed by time and decade. The authors collected a list of popular genres by decade from Wikipedia, scored music genres based on Wikipedia descriptions, and used statistical and machine learning techniques to find trends and to forecast characteristics of future music genres.

**Data Type**: tabular (genre annotations and numeric feature vectors)

**Domains**:
- Music Information Retrieval
- Natural Language Processing
- Computational Sociology

**Similar Benchmarks**:
- Music Map2

**Resources**:
- [Resource](http://personality.altervista.org/fabio.htm)
- [Resource](https://musicmap.info/)
- [Resource](https://arxiv.org/abs/1908.10275)

## 🎯 Purpose and Intended Users

**Goal**: To produce and present a dataset for computational analysis of popular music to find historical trends and to evaluate prediction of future music genre characteristics.

**Target Audience**:
- Scientific community

**Tasks**:
- Trend Analysis
- Time Series Forecasting
- Predictive Modeling

**Limitations**: Deep Learning algorithms do not perform well on this dataset because the dataset is not large enough.

## 💾 Data

**Source**: 77 genres selected from Wikipedia; genres were scored by reading Wikipedia pages and listening to samples or artists, then annotated by two independent raters.

**Size**: 77 genres; 41 annotated features per genre (feature reduction from 41 to 14 reported in experiments).

**Format**: N/A

**Annotation**: Annotated by two independent raters. Agreement measured with Cronbach's alpha: average alpha = 0.793; genre scale alpha = 0.957. Divergences were agreed upon and scores were averaged or corrected accordingly.

## 🔬 Methodology

**Methods**:
- Statistical analysis (correlation)
- Time series forecasting (backtest using 1900-2010 to predict 2011-2018)
- Machine learning: Linear Regression
- Machine learning: Support Vector Machine
- Machine learning: Multi Layer Perceptron
- Machine learning: Nearest Neighbors (IBk)
- Machine learning: Stacking meta-classifier (SVM+MLP+IBk)

**Metrics**:
- Average Accuracy (defined as proportion of predictions with absolute error < 0.1)
- Cronbach's alpha (inter-annotator agreement)
- MAE (mentioned as unsuitable)
- RMSE (mentioned as unsuitable)

**Calculation**: Average accuracy defined as a = count(|l - h| < 0.1) / count(t), where l is the label and h is the prediction and t is the year series.

**Interpretation**: Forecasting of music genres is a non-linear problem. IBk predicts the closest sequence to the annotated one and a meta-classifier with nearest neighbors is the most accurate. Deep Learning algorithms do not perform well due to dataset size. Feature reduction from 41 to 14 does not affect results obtained with IBk and meta-classifiers.

**Baseline Results**: Average accuracy by method reported in Table I: Linear Regression (LR): 0.25; Support Vector Machine (SVM): 0.375; Multi Layer Perceptron (MLP): 0.5; Nearest Neighbors (IBk): 0.5; Stacking meta-classifier: 0.75.

**Validation**: Inter-annotator agreement assessed with Cronbach's alpha (average 0.793; genre scale 0.957). Predictive models validated via backtest: training on years 1900-2010 and prediction on years 2011-2018.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
