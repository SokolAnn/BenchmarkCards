# nanoLM

## 📊 Benchmark Details

**Name**: nanoLM

**Overview**: nanoLM: an affordable LLM pre-training benchmark that facilitates a new research paradigm based on µScaling to predict pre-training loss across model scales without training large models. nanoLM is compatible with mainstream Transformer architectures (decoder-only, encoder-only, encoder-decoder), supports data-parallel strategies, and provides curated pre-training datasets with tracks of 100B, 400B, 1T, and 2T tokens drawn from existing open sources.

**Data Type**: text (pre-training token sequences)

**Domains**:
- Web Text
- Professional Knowledge (Books)
- World Knowledge (Wikipedia)
- Code (GitHub)
- Academic (arXiv)
- Question Answering (Stack Exchange)

**Languages**:
- English

**Similar Benchmarks**:
- C4
- MC4

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Enable researchers with limited computational resources to make meaningful, reliable conclusions about large-scale LLMs by predicting pre-training loss across scales via µScaling and thereby compare different model designs without training the largest models.

**Target Audience**:
- Researchers with limited computational resources
- Academic community
- Industry

**Tasks**:
- Language Model Pre-training
- Loss Prediction / Scaling Extrapolation
- Model design comparison across scales

**Limitations**: Scaling laws and µScaling require hyperparameter search within common loss basins; scaling laws can fail outside loss basins; fitting is less reliable for extremely small proxy models unless averaged across HPs; some single-GPU experiments (BERT and T5) ran out of memory at larger widths (2048) as noted.

**Out of Scope Uses**:
- Direct evaluation of pre-trained model checkpoints (nanoLM encourages pre-training new models from scratch and using pre-training loss for comparison)

## 💾 Data

**Source**: Curated from publicly accessible open-source materials previously used for large LLM training, including Falcon RefinedWeb, OpenWebText2, Books3, English Wikipedia, GitHub, arXiv, and Stack Exchange. Data sampling proportions are provided in Table 5 of the paper.

**Size**: Four tracks: 100 billion tokens; 400 billion tokens; 1 trillion tokens; 2 trillion tokens

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Grid search for µTransferable hyperparameters on a base (small) model
- µP-based hyperparameter transfer to proxy models
- Training a series of small proxy models and recording pre-training loss
- Fitting a power-law scaling function L = a * C^b + c to (loss, parameter count) pairs
- Extrapolating predicted loss for target large models using fitted power-law (µScaling)

**Metrics**:
- Pre-training Loss
- Perplexity (correlation with loss discussed)
- Floating Point Operations (FLOPs) cost ratio

**Calculation**: Fit the power-law function L = a * C^b + c to pairs (L_i, C_i) where L_i are measured training losses of proxy models and C_i are parameter counts; coefficients {a,b,c} and their standard deviations computed via scipy.optimize.curve_fit; losses measured at specified step counts (e.g., 7k, 10k, 20k steps) depending on experiment.

**Interpretation**: Lower (predicted) pre-training loss is taken as indicating a better model under the benchmark; pre-training loss is treated as a reasonable indicator of model capabilities and correlates with validation perplexity; accurate prediction of loss across scales enables comparing model designs without training large models.

**Baseline Results**: Reported predictive results include predicting the loss for a 26B (32-layer GPT) model: predicted loss 3.381 vs actual 3.41 (measured at 7k steps); predicting the loss for a 52B (64-layer GPT) model: predicted loss 2.861 vs actual 2.883 (measured at 10k steps). Efficiency: total nanoLM process cost ≈ 13.1% of one-time pre-training cost for the 26B model and ≈ 14.2% for the 52B model.

**Validation**: Empirical validation across multiple Transformer variants (GPT, Llama, BERT, T5) and datasets (C4, MC4, and the nanoLM pre-training data). Proxy models spanning ranges of widths/parameter counts were used to fit scaling laws and then compared against actual trained target models (up to 52B parameters) to assess prediction accuracy.

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
