<div align="center">

# Measuring Social Biases in Sentence Encoders

<small><em>Original: 1903.10561v1.json</em></small>

<hr style="height:2px;border-width:0;color:gray;background-color:#007acc">

</div>

## Table of Contents

- [📊 Benchmark Details](#-benchmark-details)
- [🎯 Purpose and Intended Users](#-purpose-and-intended-users)
- [💾 Data](#-data)
- [🔬 Methodology](#-methodology)
- [⚠️ Targeted Risks](#️-targeted-risks)
- [🔒 Ethical and Legal Considerations](#-ethical-and-legal-considerations)

<hr>

## 📊 Benchmark Details

<table>
<tr><td width="20%" align="center"><strong>Name</strong></td><td>
Measuring Social Biases in Sentence Encoders
</td></tr>
<tr><td width="20%" align="center"><strong>Overview</strong></td><td>
This study extends the Word Embedding Association Test (WEAT) to measure bias in sentence encoders, testing biases against gender, race, and other social constructs across various state-of-the-art models in natural language processing.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Type</strong></td><td>
Sentences
</td></tr>
<tr><td width="20%" align="center"><strong>Domains</strong></td><td>
</td></tr>
<tr><td width="20%" align="center"><strong>Languages</strong></td><td>
</td></tr>
<tr><td width="20%" align="center"><strong>Similar Benchmarks</strong></td><td>
</td></tr>
<tr><td width="20%" align="center"><strong>Resources</strong></td><td>
<ul>
<li><a href="http://github.com/W4ngatang/sent-bias">GitHub Repository</a></li>
</ul>
</td></tr>
</table>

## 🎯 Purpose and Intended Users

<table>
<tr><td width="20%" align="center"><strong>Goal</strong></td><td>
To measure the degree to which pretrained sentence encoders capture a range of social biases and explore the effectiveness of different experimental designs.
</td></tr>
<tr><td width="20%" align="center"><strong>Target Audience</strong></td><td>
<ul>
<li>Researchers in natural language processing</li>
<li>Ethics and fairness in AI communities</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Tasks</strong></td><td>
<ul>
<li>Measure bias in sentence encoders</li>
<li>Advocate for considerations of bias in NLP systems</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Limitations</strong></td><td>
Results are preliminary and cannot definitively conclude absence of bias.
</td></tr>
<tr><td width="20%" align="center"><strong>Out of Scope Uses</strong></td><td>
</td></tr>
</table>

## 💾 Data

<table>
<tr><td width="20%" align="center"><strong>Source</strong></td><td>
Various sentence templates generated for tests
</td></tr>
<tr><td width="20%" align="center"><strong>Size</strong></td><td>
N/A
</td></tr>
<tr><td width="20%" align="center"><strong>Format</strong></td><td>
N/A
</td></tr>
<tr><td width="20%" align="center"><strong>Annotation</strong></td><td>
N/A
</td></tr>
</table>

## 🔬 Methodology

<table>
<tr><td width="20%" align="center"><strong>Methods</strong></td><td>
<ul>
<li>Sentence Encoder Association Test (SEAT)</li>
<li>Word Embedding Association Test (WEAT)</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Metrics</strong></td><td>
<ul>
<li>Effect size</li>
<li>P-value</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Calculation</strong></td><td>
The SEAT uses cosine similarity to compare sets of sentence embeddings.
</td></tr>
<tr><td width="20%" align="center"><strong>Interpretation</strong></td><td>
Higher effect size indicates stronger bias; the presence of a significant p-value indicates an association.
</td></tr>
<tr><td width="20%" align="center"><strong>Baseline Results</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Validation</strong></td><td>
The results were validated by applying Holm-Bonferroni multiple testing correction.
</td></tr>
</table>

## ⚠️ Targeted Risks

<table>
<tr><td width="20%" align="center"><strong>Risk Categories</strong></td><td>
<ul>
<li>Bias evaluation validity</li>
<li>Intersectional biases in NLP</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Atlas Risks</strong></td><td>
<ul>
<li><strong>Fairness:</strong> Data bias, Output bias</li>
<li><strong>Societal Impact:</strong> Impact on affected communities</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Demographic Analysis</strong></td><td>
Focused on U.S. contexts including race and gender.
</td></tr>
<tr><td width="20%" align="center"><strong>Potential Harm</strong></td><td>
Potential reinforcement of stereotypes through bias in NLP systems.
</td></tr>
</table>

## 🔒 Ethical and Legal Considerations

<table>
<tr><td width="20%" align="center"><strong>Privacy And Anonymity</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Data Licensing</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Consent Procedures</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Compliance With Regulations</strong></td><td>
Not Applicable
</td></tr>
</table>

<hr>

<div align="center">
<p><em>This benchmark card was automatically generated.</em></p>
</div>