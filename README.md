# Organic reaction outcome prediction

Utilizes a Weisfeiler-Lehman network (attentive mechanism) to predict the products of an organic reaction given the reactants. The model identifies the reaction centers (set of atoms/bonds that change from reactant to product) and obtains the products directly from a graph-based neural network.

## Identifiers

* EOS model ID: `eos5qfo`
* Slug: `rexgen`

## Characteristics

* Input: `Compound`
* Input Shape: `List`
* Task: `Generative`
* Output: `Compound`
* Output Type: `String`
* Output Shape: `Flexible List`
* Interpretation: Products of an organic reaction

## References

* [Publication](https://arxiv.org/pdf/1709.04555v3.pdf)
* [Source Code](https://github.com/connorcoley/rexgen_direct)
* Ersilia contributor: [svolk19-stanford ](https://github.com/svolk19-stanford )

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos5qfo)

## Citation

If you use this model, please cite the [original authors](https://arxiv.org/pdf/1709.04555v3.pdf) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!