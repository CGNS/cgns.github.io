/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *\
 *      Flow Solution Quantities (SIDS Definitions Appendix A Table 11)  *
\* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

typedef enum
{
  Potential,
  StreamFunction,
  Density,
  Pressure,
  Temperature,
  EnergyInternal,
  Enthalpy,
  Entropy,
  EntropyApprox,
  DenistyStagnation,
  PressureStagnation,
  TemperatureStagnation,
  EnergyStagnation,
  EnthalpyStagnation,
  EnergyStagnationDenisty,
  VelocityX,
  VelocityY,
  VelocityZ,
  VelocityR,
  VelocityTheta,
  VelocityPhi,
  VelocityMagnitude,
  VelocityNormal,
  VelocityTangential,
  VelocitySound,
  VelocitySoundStagnation,
  MomentumX,
  MomentumY,
  MomentumZ,
  MomentumMagnitude,
  EnergyKinetic,
  PressureDynamic,
  VorticityX,
  VorticityY,
  VorticityZ,
  VorticityMagnitude,
  SkinFrictionX,
  SkinFrictionY,
  SkinFrictionZ,
  SkinFrictionMagnitude,
  VelocityAngleX,
  VelocityAngleY,
  VelocityAngleZ,
  VelocityUnitVectorX,
  VelocityUnitVectorY,
  VelocityUnitVectorZ,
  MassFlow,
  ViscosityKinematic,
  ViscosityMolecular,
  ViscosityEddyKinematic,
  ViscosityEddy,
  ThermalConductivity,
  IdealGasConstant,
  SpecificHeatPressure,
  SpecificHeatVolume,
  ReynoldsStressXX,
  ReynoldsStressXY,
  ReynoldsStressXZ,
  ReynoldsStressYY,
  ReynoldsStressYZ,
  ReynoldsStressZZ,
  LengthReference
}
FlowSolutionQuantities_t;

#define NofFlowSolutionQuantities 62

static char *FlowSolutionQuantityName[NofFlowSolutionQuantities] = {
  "Potential",
  "StreamFunction",
  "Density",
  "Pressure",
  "Temperature",
  "EnergyInternal",
  "Enthalpy",
  "Entropy",
  "EntropyApprox",
  "DenistyStagnation",
  "PressureStagnation",
  "TemperatureStagnation",
  "EnergyStagnation",
  "EnthalpyStagnation",
  "EnergyStagnationDenisty",
  "VelocityX",
  "VelocityY",
  "VelocityZ",
  "VelocityR",
  "VelocityTheta",
  "VelocityPhi",
  "VelocityMagnitude",
  "VelocityNormal",
  "VelocityTangential",
  "VelocitySound",
  "VelocitySoundStagnation",
  "MomentumX",
  "MomentumY",
  "MomentumZ",
  "MomentumMagnitude",
  "EnergyKinetic",
  "PressureDynamic",
  "VorticityX",
  "VorticityY",
  "VorticityZ",
  "VorticityMagnitude",
  "SkinFrictionX",
  "SkinFrictionY",
  "SkinFrictionZ",
  "SkinFrictionMagnitude",
  "VelocityAngleX",
  "VelocityAngleY",
  "VelocityAngleZ",
  "VelocityUnitVectorX",
  "VelocityUnitVectorY",
  "VelocityUnitVectorZ",
  "MassFlow",
  "ViscosityKinematic",
  "ViscosityMolecular",
  "ViscosityEddyKinematic",
  "ViscosityEddy",
  "ThermalConductivity",
  "IdealGasConstant",
  "SpecificHeatPressure",
  "SpecificHeatVolume",
  "ReynoldsStressXX",
  "ReynoldsStressXY",
  "ReynoldsStressXZ",
  "ReynoldsStressYY",
  "ReynoldsStressYZ",
  "ReynoldsStressZZ",
  "LengthReference"
};

/* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *\
 *      Turbulence Quantities (SIDS Definitions Appendix A Table 12)     *
\* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - */

typedef enum
{
  TurbulentDistance,
  TurbulentEnergyKinetic,
  TurbulentDissipation,
  TurbulentDissipationRate,
  TurbulentBBReynolds,
  TurbulentSANuTilde
}
TurbulenceQuantities_t;

#define NofTurbulenceQuantities 6

static char *TurbulenceQuantityName[NofTurbulenceQuantities] = {
  "TurbulentDistance",
  "TurbulentEnergyKinetic",
  "TurbulentDissipation",
  "TurbulentDissipationRate",
  "TurbulentBBReynolds",
  "TurbulentSANuTilde"
};

#define ReplaceLogicallyEquivaluentSolutionQuantity(name, index)   \
  if (strlen (name) == (unsigned) fv_name_length)                  \
{                                                                  \
      if (strncmp (fvname, name, fv_name_length) == 0)             \
{                                                                  \
          strcpy (fvname, FlowSolutionQuantityName[index]);        \
          return;                                                  \
  }                                                                \
    }

#define ReplaceLogicallyEquivaluentTurbulenceQuantity(name, index) \
  if (strlen (name) == (unsigned) fv_name_length)                  \
{                                                                  \
      if (strncmp (fvname, name, fv_name_length) == 0)             \
{                                                                  \
          strcpy (fvname, TurbulenceQuantityName[index]);          \
          return;                                                  \
  }                                                                \
    }

void ReplaceColloquialNameWithSIDSFVName (char *fvname)
{
  auto int fv_name_length = strlen (fvname);

  ReplaceLogicallyEquivaluentSolutionQuantity ("RHO", Density);
  ReplaceLogicallyEquivaluentSolutionQuantity ("P", Pressure);
  ReplaceLogicallyEquivaluentSolutionQuantity ("TF", Temperature);
  ReplaceLogicallyEquivaluentSolutionQuantity ("HF", Enthalpy);
  ReplaceLogicallyEquivaluentSolutionQuantity ("U1", VelocityX);
  ReplaceLogicallyEquivaluentSolutionQuantity ("U2", VelocityY);
  ReplaceLogicallyEquivaluentSolutionQuantity ("U3", VelocityZ);
  ReplaceLogicallyEquivaluentSolutionQuantity ("UMAG", VelocityMagnitude);
  ReplaceLogicallyEquivaluentSolutionQuantity ("VISC", ViscosityMolecular);
  ReplaceLogicallyEquivaluentSolutionQuantity ("VEFF", ViscosityEddy);
  ReplaceLogicallyEquivaluentSolutionQuantity ("COND", ThermalConductivity);
  ReplaceLogicallyEquivaluentSolutionQuantity ("CPG", SpecificHeatPressure);

  ReplaceLogicallyEquivaluentSolutionQuantity ("TKE", TurbulentEnergyKinetic);
  ReplaceLogicallyEquivaluentSolutionQuantity ("TED", TurbulentDissipation);

  return;
}

#undef ReplaceLogicallyEquivaluentSolutionQuantity
#undef ReplaceLogicallyEquivaluentTurbulenceQuantity

