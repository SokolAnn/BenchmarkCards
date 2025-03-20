<div align="center">

# GENDER-GAP Pipeline

<small><em>Original: 2308.16871v1.json</em></small>

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
GENDER-GAP Pipeline
</td></tr>
<tr><td width="20%" align="center"><strong>Overview</strong></td><td>
An automatic pipeline to characterize gender representation in large-scale datasets for 55 languages, using a multilingual lexicon of gendered person-nouns.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Type</strong></td><td>
N/A
</td></tr>
<tr><td width="20%" align="center"><strong>Domains</strong></td><td>
</td></tr>
<tr><td width="20%" align="center"><strong>Languages</strong></td><td>
<ul>
<li>English</li>
<li>Finnish</li>
<li>Zulu</li>
<li>Vietnamese</li>
<li>Ganda</li>
<li>Japanese</li>
<li>Lithuanian</li>
<li>Arab Modern Standard Arabic</li>
<li>Assamese</li>
<li>Belarusian</li>
<li>Bengali</li>
<li>Bulgarian</li>
<li>Catalan</li>
<li>Czech</li>
<li>Central Kurdish</li>
<li>Mandarin Chinese</li>
<li>Welsh</li>
<li>Danish</li>
<li>German</li>
<li>Greek</li>
<li>Irish</li>
<li>Hindi</li>
<li>Hungarian</li>
<li>Indonesian</li>
<li>Italian</li>
<li>Japanese</li>
<li>Georgian</li>
<li>Halh Mongolian</li>
<li>Kyrgyz</li>
<li>Lithuanian</li>
<li>Ganda</li>
<li>Standard Latvian</li>
<li>Marathi</li>
<li>Maltese</li>
<li>Dutch</li>
<li>Eastern Panjabi</li>
<li>Western Persian</li>
<li>Polish</li>
<li>Portuguese</li>
<li>Romanian</li>
<li>Russian</li>
<li>Slovak</li>
<li>Slovenian</li>
<li>Spanish</li>
<li>Swedish</li>
<li>Swahili</li>
<li>Tamil</li>
<li>Thai</li>
<li>Turkish</li>
<li>Ukrainian</li>
<li>Urdu</li>
<li>Northern Uzbek</li>
<li>Vietnamese</li>
<li>Yue Chinese</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Similar Benchmarks</strong></td><td>
</td></tr>
<tr><td width="20%" align="center"><strong>Resources</strong></td><td>
<ul>
<li><a href="https://github.com/facebookresearch/ResponsibleNLP/tree/main/gender_gap_pipeline">GitHub Repository</a></li>
</ul>
</td></tr>
</table>

## 🎯 Purpose and Intended Users

<table>
<tr><td width="20%" align="center"><strong>Goal</strong></td><td>
To quantify gender representation bias of multilingual texts using lexical matching as a proxy.
</td></tr>
<tr><td width="20%" align="center"><strong>Target Audience</strong></td><td>
<ul>
<li>NLP practitioners</li>
<li>Researchers in gender bias in AI</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Tasks</strong></td><td>
<ul>
<li>Characterizing gender representation in datasets</li>
<li>Quantitative reporting of gender biases</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Limitations</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Out of Scope Uses</strong></td><td>
</td></tr>
</table>

## 💾 Data

<table>
<tr><td width="20%" align="center"><strong>Source</strong></td><td>
Collected from various datasets including Common Crawl, FLORES-200, and NTREX-128.
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
<li>Lexical matching</li>
<li>Word segmentation using Stanza tokenizer</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Metrics</strong></td><td>
<ul>
<li>Gender-class scores</li>
<li>Distribution of gendered nouns</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Calculation</strong></td><td>
Scores are defined by counting occurrences of gendered nouns and dividing by the total number of words.
</td></tr>
<tr><td width="20%" align="center"><strong>Interpretation</strong></td><td>
Provides a depiction of gender representation in datasets.
</td></tr>
<tr><td width="20%" align="center"><strong>Baseline Results</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Validation</strong></td><td>
N/A
</td></tr>
</table>

## ⚠️ Targeted Risks

<table>
<tr><td width="20%" align="center"><strong>Risk Categories</strong></td><td>
<ul>
<li>Data bias</li>
<li>Underrepresentation of genders in datasets</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Atlas Risks</strong></td><td>
<ul>
<li><strong>Fairness:</strong> Data bias</li>
<li><strong>Societal Impact:</strong> Impact on affected communities</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Demographic Analysis</strong></td><td>
Analysis covers 55 languages with attention to gender representation.
</td></tr>
<tr><td width="20%" align="center"><strong>Potential Harm</strong></td><td>
Potential misrepresentation or bias in NLP systems due to conducted analysis.
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