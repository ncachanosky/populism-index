# Latin America (left-leaning) Populism Index Project

## The Index

### Introduction

The index has two sub-indices: (a) Economic populism $(EP)$ and (b) Institutional populism $(IP)$. Each sub-index is constructed with a number of components. All components are adjusted to range between 0 (less) to 100 (more) populism.

Each sub-index is the interaction of populism policies (economic or institutional) with populist motives $(POP)$. Take, for instance, income distribution. This is a typical left-leaning populist policy, but not all of income distribution policies are carried by populist regimes. A high populist index requires a populist policy (such as income distribution) executed for populist reasons. To achieve this, the index interacts economics and institutional policies with a measure of populist rhetoric.

By interacting populist policies with populist rhetoric (motives), the index separates non-populist regimes that carry out populist policies and populist regimes that do not carry out populist policies. Because the index can be dissagregated, its information can be used to study:

1. The effects of populism (the overall index)
2. The effects of economic populism
3. The effects of institutinal populism
4. The effects of economic populist policies carried out by a non-populist regime
5. The effects of institional populist policies carried out by a non-populist regime
6. The effects of a populist regime that does not carry out populist policies

### The calculation

The index is the arithmetic average of $EP$ and $IP$ adjusted for a measure of populist motives.

$\mathcal{I} = \frac{(\text{Populist rhetoric} \times \text{Populist economic policies}) + (\text{Populist rhetoric} \times \text{Populist institutional policies})}{2}$

$\mathcal{I} = \frac{(POP \cdot EP) + (POP \cdot IP)}{2}$  

$\mathcal{I} = POP \cdot \frac{EP + IP}{2}$

## Populism Rhetoric / Motives

## Economic Populism $(EP)$

### Budget Deficits

### Public Debt

### Inflation Rate

### Redistribution:

1) Relative redistribution. Measures the extent to which governments use taxes and transfers to redistribute income by comparing income inequality in the market to post-tax, post-transfer inequality.

Formula: $\frac{Gini_{Market} - Gini_{Post}}{Gini_{Market}}$

Source: The Standardized World Income Inequality Database (Solt, 2020). 

## Institutional Populism $(IP)$

The **institutional populism** $(IP)$ sub-index has four components:
1. Rule of law $(IP_1)$
2. Corruption $(IP_2)$
3. Neopatrimonialism $(IP_3)$
4. Freedom of expression $(IP_4)$

The index is the arithmetic average of the four components:  

$IP = \frac{IP_1 + IP_2 + IP_3 + IP_4}{4}$

where  

$IP_1 = \frac{IP_{1,1,} + IP_{1,2}}{2}$  

$IP_2 = \frac{IP_{2,1,} + IP_{2,2} + IP_{2,3}}{3}$

$IP_1$ and $IP_2$ include more than one source:
* V-Dem, 
* World Governance Indicators, and 
* Transparency International



## Sources

The folling tables includes the source of each component used in the index and its original databse `code name`.

| Variable                      | Source                             | Variable code  |
| ----------------------------- | ---------------------------------- | -------------- |
| **Populism rehtorical index** |                                    |                |
| Populism index                | [V-Dem][VDEM2]                     | v2xpa_popul    |
| **Economic populism**         |                                    |                |
| Income distribution           | [SWIID][SWIID]                     |                |
| **Institutional populism**    |                                    |                |
| Rule of law                   | [V-Dem][VDEM1]                     | v2x_rule       |
| Rule of Law                   | [World Governance Indicators][WGI] | RL_EST         |
| Neopatrimonialism             | [V-Dem][VDEM1]                     | v2x_neopat     |
| Corruption                    | [V-Dem][VDEM1]                     | v2x_execorr    |
| Corruption                    | [World Governance Indicators][WGI] | CC_EST         |
| Corruption                    | [Transparenty International][TI]   | CPI score      |
| Freedom of expression         | [V-Dem][VDEM1]                     | v2mecenefm_osp |




## References 
1. Solt, Frederick. 2020. “Measuring Income Inequality Across Countries and Over Time: The Standardized World Income Inequality Database.” Social Science Quarterly 101(3):1183-1199. SWIID Version 9.5, June 2023.



<!-- HYPERLINKS -->
[SWIID]: <https://fsolt.org/swiid/>

[TI]: <https://www.transparency.org/cpi>

[VDEM1]: <https://www.v-dem.net/data/the-v-dem-dataset/>
[VDEM2]: <https://v-dem.net/data/v-party-dataset/>

[WGI]: <https://info.worldbank.org/governance/wgi/>



