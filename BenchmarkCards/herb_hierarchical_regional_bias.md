# HERB (HiErarchical Regional Bias)

## 📊 Benchmark Details

**Name**: HERB (HiErarchical Regional Bias)

**Overview**: We propose a Hi-Erarchical Regional Bias evaluation method (HERB) utilising the information from the sub-region clusters to quantify the bias in pre-trained LMs. The hierarchical metric evaluates regional bias with respect to comprehensive topics and measures potential regional bias that can be propagated to downstream tasks.

**Data Type**: text (region-description sentence templates)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- regard ratio
- sentiment ratio
- individual and group fairness
- word co-occurrence score
- unmasking sequence likelihood (Kaneko and Bollegala, 2022)

**Resources**:
- [GitHub Repository](https://github.com/Bernard-Yang/HERB)
- [Resource](https://arxiv.org/abs/2211.02882)

## 🎯 Purpose and Intended Users

**Goal**: To measure and quantify hierarchical regional bias in pre-trained language models by leveraging sub-region cluster information and aggregated cluster-based sparseness, and to study how such regional bias can propagate to downstream tasks.

**Target Audience**:
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Bias evaluation
- Sentiment Analysis
- Hate Speech Detection

**Limitations**: The paper provides a hierarchical evaluation for LMs targeting the regional social groups but not corresponding mitigation methods. The provided simple template for contextual encoding may not cover all aspects of the identification of the speaker and could be further explored by localising the expressions for different regional identification.

## 💾 Data

**Source**: Descriptive word list compiled from Chaloner and Maldonado (2019), Shahid et al. (2020), and Bolukbasi et al. (2016). Regional entities selected at continent, country (region concepts from the geonamecache package), and city levels. Downstream evaluation uses public datasets IMDB (sentiment) and hatespeech18 (hate speech).

**Size**: 112 descriptive words (descriptive vector dimensionality: 112); toxic corpus for MLM experiment: 2,240 sentences (top-20 per description word). Region-level test sample counts vary by country (examples shown in Table 4, e.g., Ireland: 13,020).

**Format**: Raw text sentences (template-based: "People in [region] are [description]."), descriptive word list (text).

**Annotation**: No manual annotation; descriptive word lists compiled from prior works and templates automatically instantiated to generate region-description sentence inputs. Downstream datasets (IMDB, hatespeech18) are public and used as provided.

## 🔬 Methodology

**Methods**:
- Automated metric computation using contextualized likelihoods (f(Sij))
- Descriptive vector computation and L2 normalization
- Cluster-based sparseness calculation
- Hierarchical aggregation functions (Cw) and variant with region probability weights (Cz)
- Ablation studies on descriptive topics
- Robustness studies (word replacement)
- Downstream task evaluation (IMDB sentiment, hatespeech18 hate speech detection)
- Toxic masked language modeling continual training to observe bias score changes

**Metrics**:
- HERB (aggregated cluster-based bias score, denoted Cw and variant Cz)
- Cluster sparseness (c(R))
- Contextualized likelihood f(Sij)
- Accuracy
- Macro F1
- Prediction label change (%)

**Calculation**: Contextualized likelihood f(Sij) computed as the average of token log-probabilities for template Sij per Eq. 1. Descriptive vector v(rj) is the L2-normalized vector of f(Sij) across descriptive words (Eq. 2). Cluster sparseness c(R) is the average pairwise Euclidean distance between descriptive vectors in a cluster (Eq. 3). Aggregated hierarchical bias Cw defined using weighted pairwise distances between aggregated descriptive vectors V(r) (Eqs. 4-9). Variant Cz replaces pairwise weights with region probability-based weights computed from f(rj) (Eq. 10).

**Interpretation**: Higher HERB / higher cluster sparseness indicates greater hierarchical regional bias (more inconsistent judgements among sub-regions). The aggregated HERB score summarises bias across hierarchical levels; increases in HERB during toxic MLM training indicate integration of more biased corpus into the model.

**Baseline Results**: Reported model-level HERB results (Table 1): BERT Base Cw overall 2.3223; ALBERT Base-V2 Cw overall 3.3045; RoBERTa Base Cw overall 3.2274; BART Base Cw overall 0.5732. (Paper notes: all statistics in Table 1 are multiplied by 1e3.)

**Validation**: Validated via ablation studies (removing descriptive topics), robustness tests replacing descriptive words, downstream task evaluation showing prediction changes when adding regional prefixes (IMDB, hatespeech18), and a toxic MLM continual training experiment showing HERB scores increase as biased sentences are added.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on Jobs, Impact on affected communities

**Demographic Analysis**: Provides continent-level and country-level breakdowns of HERB scores, visualizations of country-level representations (UMAP), and analysis of prediction changes on downstream tasks by country.

**Potential Harm**: ['Stereotyping and offensive content toward regional groups (content warning noted in paper)', 'Negative societal impacts on minorities', 'Potential impact on job outcomes (example: downgrading of resumes referenced)', 'Misclassification or altered predictions in downstream tasks (e.g., increased hate speech predictions for certain regions)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
