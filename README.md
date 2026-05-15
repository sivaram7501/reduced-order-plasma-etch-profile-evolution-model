# **Plasma Etch Anisotropy Modeling Framework**

Physics-informed reduced-order plasma etching model for studying anisotropy evolution, ion transport, angular scattering, ARDE effects, and sidewall passivation in ICP plasma etching systems.

## Overview
This project presents a compact plasma etching simulation framework developed using physics-based reduced-order modeling concepts.	 The model predicts trench evolution and anisotropy behavior under varying plasma process conditions including chamber pressure, bias power, source power, and passivation effects.

## The framework focuses on the transport competition between:
- Bottom directional ion flux 
- Sidewall ion flux
- Angular ion scattering
- Aspect Ratio Dependent Etching (ARDE)
- Passivation-controlled lateral suppression

The objective of the model is not high-fidelity plasma simulation, but physically interpretable trend prediction and process knob analysis.

## Physics Included
The model currently incorporates:

- Electron temperature scaling
- Plasma density scaling
- Bohm velocity
- Ion flux transport
- Ion energy attenuation
- Pressure-induced angular ion scattering
- Bottom vs sidewall flux decomposition
- Aspect Ratio Dependent Etching (ARDE)
- Sidewall passivation suppression
- Dynamic trench geometry evolution
- Anisotropy evolution

## Governing Concepts
- Ion Flux
	- Γi=ni*cs
	​
- Bohm Velocity
	- cs=sqrt(kTe/mi)
	​
- Angular Spread
	- θ=θmax*(1−exp(kp/Ei))

- Bottom Ion Flux
	- Γb=Γ0cos(θ)exp(kARp/Ei)
	​
- Sidewall Ion Flux
	- Γsw=Γ0*sin(θ)(1−exp(kARp/Ei))

## Outputs
The model predicts:

- Vertical trench depth
- Lateral trench depth
- Angular ion spread
- Ion energy evolution
- Bottom ion flux
- Sidewall ion flux
- Aspect ratio evolution
- Etch anisotropy
- Project Goals

## This project was developed to:
- Learn plasma transport modeling
- Understand anisotropy formation mechanisms
- Explore compact plasma process modeling
- Study process knob influence on etching behavior
- Build physics-informed semiconductor process simulations from scratch
- Current Limitations

# This is a reduced-order trend-predictive model and does not include:
- Full plasma chemistry
- PIC/MCC simulation
- Detailed sheath dynamics
- Monte Carlo transport
- Surface reaction kinetics
- Experimental calibration
- Full TCAD-level physics

The framework is intended for physical understanding, compact modeling exploration, and educational research purposes.

## Future Improvements
Planned future additions:

- [ ] Dynamic passivation evolution
- [ ] Radical transport modeling
- [ ] Feature charging effects
- [ ] Ion energy distribution functions
- [ ] Dynamic trench profile visualization
- [ ] Full profile evolution
- [ ] Recipe optimization framework
- [ ] Experimental validation


## Research Focus

Main research direction:

Influence of plasma process knobs on anisotropy formation in ICP plasma etching systems using reduced-order transport modeling.

Author

Siva
- Mechanical Engineer | Semiconductor Process Modeling Enthusiast


