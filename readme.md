# Latin America Left-Leaning Populism Index Project

> :small_red_triangle: PROJECT UNDER DEVELOPMENT :small_red_triangle:

## The Index

### Introduction

The **Latin America Left-Leaning Populism Index** is a measure of active populist policies. The index has two sub-indices:

* Economic populism $(EP)$
* Institutional populism $(IP)$.

Each sub-index is the result of interacting a measure of populist *rhetoric* with typical left-leaning policies. This interaction produces two outcomes:

* Take into consideration if populist *rhetoric* becomes *action*
* Take into consideration if typical populist policies are executed for *populist reasons*

Each sub-index is the interaction of populism policies (economic or institutional) with populist motives $(POP)$. Take, for instance, income distribution. This is a typical left-leaning populist policy, but not all income distribution policies are carried by populist regimes. A high populist index requires a populist policy (such as income distribution) executed for populist reasons. To achieve this, the index interacts with economics and institutional policies with a measure of populist rhetoric.

Each sub-index is constructed with several areas. All areas are adjusted to range between 0 (less) to 100 (more) populism and equally weighted.

By interacting populist policies with populist rhetoric (motives), the index separates non-populist regimes that carry out populist policies and populist regimes that do not carry out populist policies. Because the index can be disaggregated, its information can be used to study:

1. The effects of populism (the overall index)
2. The effects of economic populism
3. The effects of institutional populism
4. The effects of economic populist policies carried out by a non-populist regime
5. The effects of institutional populist policies carried out by a non-populist regime
6. The effects of a populist regime that does not carry out populist policies

### Methodology

The index is the arithmetic average of $EP$ and $IP$ adjusted to measure populist motives.

$\mathcal{I} = \frac{(\text{Populist rhetoric} \times \text{Populist economic policies}) + (\text{Populist rhetoric} \times \text{Populist institutional policies})}{2}$

$\mathcal{I} = \frac{(POP \cdot EP) + (POP \cdot IP)}{2} = P \cdot \left(\frac{EP + IP}{2}\right)$

Where `POP` is a measure of populist rhetoric and `EP` and `IP` denote economic and institutional populism respectively.

Subsequently, each sub-index is the arithmetic average of their components.

### Populism rhetoric

The measure of *populism rhetoric* is the V-Party Populism index. The index data is re-escaled from (0, 1) to (0, 100). 

The V-Party Populism Index measures the populist rhetoric of active political parties in each country. The index uses the index corresponding to the head of state's political party affiliation. For years where there is a change of party in the executive office, the data for the party with the majority of days in office is used.

### Economic Populism $(EP)$

The Economic Populism Sub-Index looks at the following four (4) economic policy areas typically observed in Latin American populist regimes:

1. Business (and labor market) regulations
2. Government interference
3. Monetary (and financial) freedom
4. Freedom to trade (internationally)

$$
EP = P \cdot \left(\frac{\text{Business regulations + Gov. interferences + Monetary freedom + Freedom to trade}}{4}\right) = P \cdot \left(\frac{EP_1 + EP_2 + EP_3 + EP_4}{4}\right)
$$

The contributors to each economic policy area are the following

* EP_1 = (EP_11 + EP_12 + EP_13)/3
* EP_2 = (EP_21 + EP_22)/2
* EP_3 = (EP_31 + EP_32 + EP_33)/3
* EP_4 = (EP_41 + EP_42)/2

where:

* EP_11 = Heritage's Foundation Index of Economic Freedom: Business freedom.
* EP_12 = Fraser's Economic Freedom of the World: Labor Market Regulations (5A).
* EP_13 = Fraser's Economic Freedom of the World: Business Regulations (5C).
* EP_21 = Fraser's Economic Freedom of the World: Transfers and Subsidies (1B).
* EP_22 = Fraser's Economic Freedom of the World: State Ownership (IE).
* EP_31 = Heritage's Foundation Index of Economic Freedom: Monetary Freedom.
* EP_32 = Heritage's Foundation Index of Economic Freedom: Financial Freedom.
* EP_33 = Fraser's Economic Freedom of the World: Foreign Currency and Bank Accounts (3D).
* EP_41 = Heritage's Foundation Index of Economic Freedom: Trade Freedom.
* EP_42 = Fraser's Economic Freedom of the World: Freedom to Trade Internationally (4).

### Institutional Populism $(IP)$

The Institutional Populism Sub-Index looks at the following five (5) institutional areas typically observed in Latin American populist regimes:

1. Rule of Law
2. Corruption
3. Neopatrimonialism
4. Freedom of the Expression
5. Property Rights


$$
IP = \frac{\text{Rule of Law + Corruption + Neopatrimonialism + Freedom of Expression + Property Rights}}{5} = \frac{IP_1 + IP_2 + IP_3 + IP_4 + IP_5}{5}
$$

The contributors to each economic policy area are the following

* IP_1 = (IP_11 + IP_12 + IP_13 + IP_14)/4
* IP_2 = (IP_21 + IP_22)/2
* IP_3 = IP_31
* IP_4 = IP_41
* IP_5 = IP_51

where:

* IP_11 = V-Dem: Rule of Law.
* IP_12 = V-Dem: Judiciary Constraints on the Executive.
* IP_13 = V-Dem: Legislative Constraints on the Executive.
* IP_14 = WGI: Rule of Law.
* IP_21 = V-Dem: Corruption.
* IP_22 = WGI: Control of Corruption.
* IP_31 = V-Dem: Neopatrimonialism.
* IP_41 = V-Dem: Freedom of Expression.
* IP_51 = Heritage's Foundation Index of Economic Freedom: Property Rights.


## Sources

The following tables include the source of each component used in the index and its original database `code name`.

| Variable                                       | Source                               | Variable code     |
| :--------------------------------------------- | :----------------------------------- | :---------------- |
| **Populism rhetorical index**                  |                                      |                   |
| Populism index                                 | [V-Dem][VDEM1]                       | v2xpa_popul       |
| **Economic populism**                          |                                      |                   |
| EP_11: Business Freedom                        | [Index of Economic Freedom][HIEF]    | Business Freedom  |
| EP_12: Labor Markert Regulations               | [Economic Freedom of the World][EFW] | 5A                |
| EP_13: Business Regulations                    | [Economic Freedom of the World][EFW] | 5C                |
| EP_21: Transfers and Subsidies                 | [Economic Freedom of the World][EFW] | 1B                |
| EP_22: State Ownership                         | [Economic Freedom of the World][EFW] | IE                |
| EP_31: Monetary Freedom                        | [Index of Economic Freedom][HIEF]    | Monetary Freedom  |
| EP_32: Financial Freedom                       | [Index of Economic Freedom][HIEF]    | Financial Freedom |
| EP_33: Foreign Currency and Bank Accounts      | [Economic Freedom of the World][EFW] | 3D                |
| EP_41: Trade Freedom                           | [Index of Economic Freedom][HIEF]    | Trade Freedom     |
| EP_42: Freedom to Trade Internationally        | [Economic Freedom of the World][EFW] | 4                 |
| **Institutional populism**                     |                                      |                   |
| IP_11: Rule of law                             | [V-Dem][VDEM2]                       | v2x_rule          |
| IP_12: Judiciary Consraints on the Executive   | [V-Dem][VDEM2]                       | v2x_jucon         |
| IP_13: Legislative Consraints on the Executive | [V-Dem][VDEM2]                       | v2xlg_legcon      |
| IP_14: Rule of Law                             | [World Governance Indicators][WGI]   | RL_EST            |
| IP_21: Corruption                              | [V-Dem][VDEM2]                       | 2x_execorr        |
| IP_22: Control of Corruption                   | [World Governance Indicators][WGI]   | CC_EST            |
| IP_31: Neopatrimonialism                       | [V-Dem][VDEM2]                       | 2x_neopat         |
| IP_41: Freedom of Expression                   | [V-Dem][VDEM2]                       | v2mecenefm_osp    |
| IP_51: Property Rights                         | [Index of Economic Freedom][HIEF]    | Property Rights   |




<!-- HYPERLINKS -->
[VDEM1]: <https://v-dem.net/data/v-party-dataset/>
[VDEM2]: <https://www.v-dem.net/data/the-v-dem-dataset/>
[HIEF]: <https://www.heritage.org/index/>
[EFW]: <https://www.fraserinstitute.org/economic-freedom/map>
[WGI]: <https://info.worldbank.org/governance/wgi/>



