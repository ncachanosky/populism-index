# Latin America (left-leaning) Populism Index Project

## The Index
The index has two sub-indices: (a) Economic populism $(EP)$ and (b) Institutional populism $(IP)$. Both sub-indices range from 0 (less) to 100 (more) populism.

Each sub-index is the interaction of populism policies with populist motives. Take, for instance, income distribution. This is a typical left-leaning populist policy, but not all of income distribution policies are carried by populist regimes. A high populist index requires a populist policy (such as income distribution) executed for populist reasons. To achieve this, the index interacts economics and institutional policies with a measure of populist rhetoric.

The index is the arithmetic average of $EP$ and $IP$ adjusted for a measure of populist motives.

$$
\mathcal{I} = \frac{EP + IP}{2}
$$

where:

$$
\begin{align}
EP &= \text{Populist rhetoric} \times \text{Populist economic policies} \\
IP &= \text{Populist rhetoric} \times \text{Populist institutional policies}
\\end{align}
$$

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

Each component ranges between 0 (less populism) and 100 (more populism). The index is the arithmetic average of the four components:  

$IP = \frac{IP_1 + IP_2 + IP_3 + IP_4}{4}$

where  

$IP_1 = \frac{IP_{1,1,} + IP_{1,2}}{2}$  

$IP_2 = \frac{IP_{2,1,} + IP_{2,2}}{2}$

$IP_1$ and $IP_2$ include two measures of *corruption* and *rule of law*, V-Dem and World Governance Indicators.



## Sources

| VARIABLE                      | SOURCE         | VARIABLE CODE  |
| ----------------------------- | -------------  | -------------- |
| **Populism rehtorical index** |                |                |
| Populism index                | [V-Dem][VDEM2] | v2xpa_popul    |
| **Economic populism**         |                |                |
| Income distribution           | [SWIID][SWIID] |                |
| **Institutional populism**    |                |                |
| Rule of law                   | [V-Dem][VDEM1] | v2x_rule       |
| Rule of Law                   | [WGI][WGI]     | RL_EST         |
| Neopatrimonialism             | [V-Dem][VDEM1] | v2x_neopat     |
| Corruption                    | [V-Dem][VDEM1] | v2x_execorr    |
| Corruption                    | [WGI][WGI]     | CC_EST         |
| Freedom of expression         | [V-Dem][VDEM1] | v2mecenefm_osp |




## References 
1. Solt, Frederick. 2020. “Measuring Income Inequality Across Countries and Over Time: The Standardized World Income Inequality Database.” Social Science Quarterly 101(3):1183-1199. SWIID Version 9.5, June 2023.



<!-- HYPERLINKS -->
[SWIID]: <https://fsolt.org/swiid/>

[VDEM1]: <https://www.v-dem.net/data/the-v-dem-dataset/>
[VDEM2]: <https://v-dem.net/data/v-party-dataset/>

[WGI]: <https://info.worldbank.org/governance/wgi/>

