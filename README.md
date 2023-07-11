# S2DV HepG2 toxicity

The model uses Word2Vec, a natural language processing technique to represent SMILES strings. The model was trained on over <2000 small molecules with associated experimental HepG2 cytotoxicity data (IC50) to classify compounds as HepG2 toxic (IC50 <= 30 uM) or non-toxic. Data was gathered from the public repository ChEMBL.

## Identifiers

* EOS model ID: `eos2fy6`
* Slug: `s2dv-hepg2-toxicity`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Experimental value`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of HepG2 Toxicity (IC50 < 30 uM)

## References

* [Publication](https://pubmed.ncbi.nlm.nih.gov/35062019/)
* [Source Code](https://github.com/NTU-MedAI/S2DV)
* Ersilia contributor: [emmakodes](https://github.com/emmakodes)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos2fy6)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos2fy6.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos2fy6) (AMD64, ARM64)

## Citation

If you use this model, please cite the [original authors](https://pubmed.ncbi.nlm.nih.gov/35062019/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a Apache-2.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!