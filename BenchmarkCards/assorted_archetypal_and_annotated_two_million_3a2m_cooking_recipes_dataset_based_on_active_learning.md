# Assorted, Archetypal and Annotated Two Million (3A2M) Cooking Recipes Dataset based on Active Learning

## 📊 Benchmark Details

**Name**: Assorted, Archetypal and Annotated Two Million (3A2M) Cooking Recipes Dataset based on Active Learning

**Overview**: We present a novel dataset of two million culinary recipes labeled in respective categories leveraging the knowledge of food experts and an active learning technique. The dataset was constructed by collecting recipes from the RecipeNLG dataset, manually labeling 300,000 recipes by three human experts into nine categories, and categorizing the remaining 1,900,000 recipes using an active learning method combining Query-by-Committee and Human-In-The-Loop approaches. Each recipe is categorized and has an associated confidence score.

**Data Type**: text (recipe texts with Named Entity Recognition annotations and genre labels)

**Domains**:
- Natural Language Processing
- Culinary / Food Science

**Languages**:
- English

**Similar Benchmarks**:
- RecipeNLG
- Recipe1M+

**Resources**:
- [Resource](https://tinyurl.com/3zu4778y)

## 🎯 Purpose and Intended Users

**Goal**: Construct an annotated dataset of two million culinary recipes categorized into nine genres using domain experts and active learning so the research community can perform tasks such as recipe genre classification, recipe generation, new recipe creation, and NLP tasks like named entity recognition, part-of-speech tagging, and semantic role labeling.

**Target Audience**:
- Research community
- Machine learning researchers
- Medical sectors working with food nutrition

**Tasks**:
- Text Classification (Recipe Genre Classification)
- Text Generation (Recipe Generation and New Recipe Creation)
- Named Entity Recognition
- Part-of-Speech Tagging
- Semantic Role Labeling

**Limitations**: Inter-annotator agreement is moderate: Inter-Rater Reliability (IRR) = 50.3976667% on 300K expert-annotated data; Fleiss Kappa = 0.4965 on 300K and approximately 0.56026 reported for the large dataset. Annotation is subject to expert subjectivity. The authors did not incorporate large pre-trained models like BERT into the active learning procedure due to resource constraints.

## 💾 Data

**Source**: Collected from the RecipeNLG dataset (recipes aggregated from cookbooks, blogs, and recipe websites).

**Size**: 2,200,000 recipes (300,000 manually annotated; 1,900,000 annotated via active learning).

**Format**: N/A

**Annotation**: Manual annotation by three human experts (trustworthiness > 86.667%) for 300,000 recipes assigning one of nine genres using Named Entity Recognition (NER); remaining 1,900,000 recipes annotated via Active Learning using a Query-by-Committee approach with an ensemble of classifiers (Logistic Regression, Support Vector Machine, Naive Bayes, Multi-Layer Perceptron, Random Forest) and Human-in-the-Loop verification when committee did not reach consensus.

## 🔬 Methodology

**Methods**:
- Active Learning (Query-by-Committee)
- Human-in-the-loop annotation
- Ensemble of classifiers (Logistic Regression, Support Vector Machine, Naive Bayes, Multi-Layer Perceptron, Random Forest)
- Inter-rater reliability analysis
- Fleiss Kappa agreement measurement
- Anderson-Darling statistical test
- ROC and Precision-Recall curve analysis

**Metrics**:
- Fleiss Kappa
- Inter-Rater Reliability (IRR)
- Annotator Trustworthiness Score
- Confidence Score
- Receiver Operating Characteristic (ROC) curves
- Precision-Recall curves
- Accuracy
- Sensitivity
- Specificity
- Precision
- Anderson-Darling test statistic and p-value

**Calculation**: Fleiss Kappa computed over 300,000 expert-annotated samples. IRR computed as percent agreement among three annotators on 300,000 samples. Trustworthiness score computed from 470 labeled samples including 30 control samples selected by domain experts. Confidence scores aggregated based on annotator trustworthiness and majority/most-confident responses. In active learning, batches of 50,000 samples were predicted per iteration; labels accepted when more than three classifiers agreed (Query-by-Committee), otherwise instances were resolved via Human-in-the-Loop. ROC and Precision-Recall curves used to determine classifier cutoff values. Anderson-Darling test applied on sample distributions to obtain p-values.

**Interpretation**: Authors use standard interpretation for Fleiss Kappa (0.20 = poor, 0.20 = fair, 0.41 = moderate, 0.61 = good, 0.81 = very good). The dataset's Fleiss Kappa (~0.4965 on 300K; ~0.56026 overall) is interpreted as moderate agreement. IRR of ~50.3977% is described as mild. Lower p-values in AD test indicate evidence against the null hypothesis.

**Validation**: Validation included iterative active learning with retraining after each labeling iteration, Query-by-Committee acceptance when >3 classifiers agreed, and Human-in-the-Loop resolution for disagreements. Statistical validation included Inter-Rater Reliability, Fleiss Kappa on expert annotations, Trustworthiness scores for annotators, Confidence scores for annotations, ROC/Precision-Recall analysis for classifier performance, and Anderson-Darling tests for distribution analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Decision bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
