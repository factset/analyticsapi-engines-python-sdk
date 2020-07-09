4.0.0 (06/17/2020)

Supported API versions:
* v2

Summary:
* Adding support for new features

Breaking changes:
* Additional parameter in calculation object constructor

Functionality Additions:
* Publisher API calculation and document lookup
* New componentdetail parameter for PA and Vault calculation
* Interactive endpoints for PA, SPAR and Vault APIs

Bug Fixes:
* No changes

-----------------------

3.0.0 (12/02/2019)

Supported API versions:
* v2

Summary:
* Making SDK independent of the API version.

Breaking changes:
* API version is removed from the package name.

Functionality Additions:
* No changes

Bug Fixes:
* No changes

-----------------------

v2-2.0.0 (09/19/2019)

Supported API versions:
* v2

Summary:
* Update class and property names.

Breaking changes:
* Class Name
  * OutstandingCalculation -> CalculationStatusSummary
  * CalculationParameters -> Calculation
  * OutstandingCalculations -> CalculationStatus (class)
  * CalculationStatus (enum) -> UnitStatus
  * Calculation -> CalculationUnitStatus
  * AccountList -> AccountDirectories
  * ComponentListEntity -> ComponentSummary
  * PAComponentEntity -> PAComponent
  * VaultComponentEntity -> VaultComponent
  * ConfigurationItem -> VaultConfigurationSummary
  * ConfigurationRoot -> VaultConfiguration
  * DateSettings -> DateParametersSummary
  * DocumentList -> DocumentDirectories
  * ComponentDateSettings (pa) -> PADateParameters
  * ComponentDateSettings (vault) -> VaultDateParameters

* Properties
  * pointscount -> points
  * defaultAccounts (ComponentAccount) -> accounts (PAIdentifier)
  * defaultBenchmarks (ComponentBenchmark) -> benchmarks (PAIdentifier)
  * defaultAccount (VaultCalculationAccount) -> accounts (VaultIdentifier)
  * defaultBenchmark (ComponentBenchmark) -> benchmark (VaultIdentifier)
  * currency (PAComponentEntity/VaultComponentEntity) -> currencyisocode (PAComponent/VaultComponent)

* Methods
  * getAllCalculationStatusSummaries -> getCalculationStatusSummaries
  * getAllPAColumnStatistics -> getPAColumnStatistics
  * getAllPAColumns -> getPAColumns
  * getPAColumn -> getPAColumnById
  * getAllPACurrencies -> getPACurrencies
  * getAllPAFrequencies -> getPAFrequencies
  * getAllSPARFrequencies -> getSPARFrequencies
  * getAllVaultFrequencies -> getVaultFrequencies
  * getAllPAGroups -> getPAGroups
  * getAllCalculations -> getAllCalculationStatusSummaries
  * getCalculationById -> getCalculationStatusById

* Headers
  * X-FactSet-Api-PointsCount-Limit -> X-FactSet-Api-Points-Limit
  * X-FactSet-Api-PointsCount-Remaining -> X-FactSet-Api-Points-Remaining

* Currencies
  * Change response from List to Dictionary with currencyisocode as key

Functionality Additions:
* New Property snapshot in PAComponent & VaultComponent.

Bug Fixes:
* No changes.

-----------------------

v2-1.0.0 (08/30/2019)

Supported API versions:
* v2

Summary:
* Releasing first version of Engines API(v2).

Breaking changes:
* No changes

Functionality Additions:
* Supports PA, SPAR and Vault calculations.

Bug Fixes:
* No changes
